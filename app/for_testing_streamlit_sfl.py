import requests
import re
from dotenv import load_dotenv, dotenv_values
import json
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import html2text
from openai import OpenAI



app = Flask(__name__)
CORS(app)

load_dotenv()
config = dotenv_values(".env")

# Gets Snov token
@app.route("/get_snov_token", methods=['GET'])
def get_snov_token_route():
    clientId = config.get("snov_clientId")
    clientSecret = config.get("snov_clientSecret")
    tokenEndpoint = 'https://api.snov.io/v1/oauth/access_token'

    payload = {
        'grant_type': 'client_credentials',
        'client_id': clientId,
        'client_secret': clientSecret
    }

    response = requests.post(tokenEndpoint, data=payload)
    if response.status_code == 200:
        token_data = response.json()
        return jsonify({'access_token': token_data.get('access_token')})
    else:
        return jsonify({'error': 'Failed to obtain token'}), response.status_code

# The `ping_snov` function is designed to interact with the Snov.io API to retrieve email addresses associated with a given domain. 
# Queries Snov.io's API for emails related to the specified domain, filtering the results to include only verified emails. 
# The function returns a JSON response containing these verified emails. 

@app.route("/ping_snov/<domain>", methods=['GET'])
def ping_snov(domain):
    print("Attempting to obtain Snov.io access token...")
    token_response = get_snov_token_route()
    if not token_response:
        print("No response received from get_snov_token_route.")
        abort(500, description="Failed to obtain Snov.io access token.")
    else:
        print("Response received from get_snov_token_route.")
    token_data = token_response.get_json()
    access_token = token_data.get('access_token')
    if not access_token:
        print("Access token not found in the response.")
        abort(500, description="Failed to obtain access token from Snov.io.")
    else:
        print(f"Access token obtained: {access_token}")

    params = {
        'access_token': access_token,
        'domain': domain,
        'type': 'all',
        'limit': 10,
        'lastId': 0,
    }

    res = requests.get('https://api.snov.io/v2/domain-emails-with-info', params=params)
    if res.status_code != 200:
        error_message = f"Failed to get emails from Snov.io. Status code: {res.status_code}, Response: {res.text}"
        app.logger.error(error_message)  # Log the detailed error
        abort(res.status_code, description=error_message)
    response_data = res.json()
    
    # Extracting verified emails only
    verified_emails = [item['email'] for item in response_data.get('data', []) if item['status'] == 'verified']
    return jsonify(verified_emails)

# This endpoint is responsible for fetching and returning a list of user-created lists from the Snov.io API. 
# It retrieves these lists by making a GET request to the Snov.io 'get-user-lists' endpoint using the access token obtained from the Snov.io authentication process. 
# The response is a JSON object containing an array of lists, each list having an 'id' and a 'name'. This is useful for applications that need to display or interact with these user lists, such as adding new prospects to a specific list.
@app.route("/user_lists", methods=['GET'])
def user_lists():
    token_response = get_snov_token_route()
    if not token_response:
        abort(500, description="Failed to obtain Snov.io access token.")
    token_data = token_response.get_json()
    access_token = token_data.get('access_token')
    if not access_token:
        abort(500, description="Failed to obtain access token from Snov.io.")
    params = {
    'access_token':access_token
    }

    res = requests.get('https://api.snov.io/v1/get-user-lists', params=params)
    if res.status_code != 200:
        abort(res.status_code, description="Failed to get user lists from Snov.io.")
    user_lists = [{'id': item['id'], 'name': item['name']} for item in json.loads(res.text)]
    return jsonify(user_lists)

#     This endpoint handles the addition of a new prospect to a specified list in Snov.io.
#     It expects a POST request with JSON data containing the prospect's email, first name, and the ID of the list they should be added to.
@app.route("/add_prospect_to_list/", methods=['POST'])
def add_prospect_to_list():
   
    data = request.get_json()  # Adjusted for clarity and consistency
    if not data:
        abort(400, description="Invalid request. Please provide email, firstName, and listId in JSON format.")
    
    email = data.get('email')
    firstName = data.get('firstName')
    listId = data.get('listId')
    
    # Validate required fields
    if not all([email, firstName, listId]):
        abort(400, description="Missing required fields. Please include email, firstName, and listId.")
    
    token_response = get_snov_token_route()
    if not token_response:
        abort(500, description="Failed to obtain Snov.io access token.")
    token_data = token_response.get_json()
    access_token = token_data.get('access_token')
    if not access_token:
        abort(500, description="Failed to obtain access token from Snov.io.")
    
    params = {
        'access_token': access_token,
        'email': email,
        'firstName': firstName,
        'listId': listId
    }

    res = requests.post('https://api.snov.io/v1/add-prospect-to-list', json=params)  # Changed to json=params to ensure proper request formatting
    if res.status_code != 200:
        abort(res.status_code, description=f"Failed to add prospect to list in Snov.io. Error: {res.text}")
    return jsonify(res.json())  # Simplified response handling

# Extract navigation links from a specified domain name. 
# It performs an HTTP GET request to the domain, converts the HTML content to Markdown format, and then uses regular expressions to find and list all navigation links present in the Markdown. 
# Each link is stored as a dictionary with 'text' and 'url' keys, representing the link text and the hyperlink respectively. 

def scrape_links(domain_name):
    """
    Function to scrape the given domain name, convert the page into markdown, and find the links in the navigation.
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        # Ensure the domain name is prefixed with https://www.
        if not domain_name.startswith(('http://', 'https://')):
            domain_name = 'https://www.' + domain_name
        response = requests.get(domain_name, headers=headers)
        if response.status_code == 200:
            # Convert HTML to Markdown
            markdown = html2text.HTML2Text().handle(response.text)
            # Use regular expressions to find links in the markdown
            links = re.findall(r'\[([^\]]+)\]\((http[s]?://[^\s]+|/[^\s]+)\)', markdown)
            # Prepare a list to hold both text and URL of the links
            navigation_links = [{"text": text, "url": url} for text, url in links]
            # print(navigation_links)
            return navigation_links
        else:
            print(f"Failed to fetch {domain_name} with status code {response.status_code}")
            return []
    except requests.exceptions.SSLError as ssl_error:
        print(f"SSL Error occurred while fetching {domain_name}: {ssl_error}")
        return []
    except Exception as e:
        print(f"An error occurred while fetching {domain_name}: {e}")
        return []
    

#     Takes in an array of navigation links and uses OpenAI to determine which link likely contains the list of attorneys/people working at the firm.


def find_specific_links(navigation_links):
   
    client = OpenAI()
    system_message = """
             I am looking for links in a site's navigation. I will provide a list of links from the top to the bottom of the site. Weigh the links at the beginning higher than ones at the bottom of the list. Given a list of website navigation links, identify the link (keep in mind that i'm providing the full link, but in my examples im only providing the subdirectory) that most likely contains the list of attorneys or people working at the firm (this usually looks like /attorney, /people, or /who-we-are). Here are the links:
             
             Which link contains the list of attorneys? 
             
             Only return a json with 1 key, 
              call this 'lawyer link' the link for the url that contains the list of lawyers that work at the firm. The links should be full links, including the domain. Do not make up any links, only use it from the list provided. If links for certain pages dont exist then ignore that page.
             """
    # Convert navigation links to a string format for the prompt
    formatted_links = "\n".join([f"- {link['text']}: {link['url']}" for link in navigation_links])
    full_prompt = f"{system_message}\n{formatted_links}"

    # Pass the system message and formatted prompt to the LLM
    response = client.chat.completions.create(
        # model="gpt-4-turbo-preview",
        model="gpt-3.5-turbo-0125",
        messages=[
            # {"role": "system", "content": system_message},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0, 
        response_format={"type": "json_object"}
    )

    # Extract and print the response content
    content = response.choices[0].message.content
    print(content)


    # Return the response content
    return content


# @app.route("/find_nav_links", methods=['POST'])
def find_nav_links(navigation_links):
   
    client = OpenAI()
    system_message = """
            I am looking for links in a site's navigation. I will provide a list of links from the top to the bottom of the site. Weigh the links at the beginning higher than ones at the bottom of the list. Given a list of website navigation links, identify the link (keep in mind that i'm providing the full link, but in my examples im only providing the subdirectory) that most likely contains the list of attorneys or people working at the firm (this usually looks like /attorney, /people, or /who-we-are), the link to practice areas (this usually looks like /practice-areas or /what-we-do),the link to about us (usually looks like /about-us), and links to testimonials (usually look like /testimonials). Here are the links:
             
             Which link contains the list of attorneys? Which link leads to practice areas? Which link leads to about us? Which link leads to testimonials?
             
             
             Only return a json with 2 keys: 
             1) call this key, 'all nav links' and have an array of the links that are in the navigation,  The links should be full links, including the domain. Do not make up any links, only use it from the list provided. If links for certain pages dont exist then ignore that page.
             2) call this 'lawyer link' the link for the url that contains the list of lawyers that work at the firm. The links should be full links, including the domain. Do not make up any links, only use it from the list provided. If links for certain pages dont exist then ignore that page.
             """
    # Convert navigation links to a string format for the prompt
    formatted_links = "\n".join([f"- {link['text']}: {link['url']}" for link in navigation_links])
    full_prompt = f"{system_message}\n{formatted_links}"

    # Pass the system message and formatted prompt to the LLM
    response = client.chat.completions.create(
        # model="gpt-4-turbo-preview",
        model="gpt-3.5-turbo-0125",
        messages=[
            # {"role": "system", "content": system_message},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0, 
        response_format={"type": "json_object"}
    )

    # Extract and print the response content
    content = response.choices[0].message.content
    print(content)


    # Return the response content
    return content



#     Takes a URL that contains the names of the attorneys that work at the firm,
#     converts that page to markdown, passes it to OpenAI, and extracts all the names
#     of the people who work at the firm.

def extract_attorney_names(attorney_page_url):
   
    try:
        # Fetch the HTML content from the URL
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        response = requests.get(attorney_page_url, headers=headers)
        if response.status_code == 200:
            # Convert HTML to Markdown
            markdown = html2text.HTML2Text().handle(response.text)
            client = OpenAI()
            # Construct the prompt to extract names
            prompt = "Extract and only return, in an array,  all the names of the people who work at the firm from the following text:\n\n" + markdown
            # Pass the prompt to the LLM
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0,
                # response_format={"type": "json_object"}
            )
            # Extract and return the names from the response
            names = response.choices[0].message.content
            print(names)
            return names
        else:
            print(f"Failed to fetch {attorney_page_url} with status code {response.status_code}")
            return []
    except Exception as e:
        print(f"An error occurred while processing {attorney_page_url}: {e}")
        return []
    
# This function takes a POST request containing two lists: emails and attorneyNames.
# It constructs a prompt for OpenAI's GPT model to match attorney names with their corresponding emails.
# The function then sends this prompt to the GPT model and receives a list of matched names and emails in JSON format.
# Finally, it returns this list as a JSON response to the client.

@app.route("/match_emails_with_names", methods=['POST'])
def match_emails_with_names():
    # Parse the JSON data sent in the request
    data = request.get_json()
    
    # Extract emails and attorneyNames from the data
    emails = data.get('emails', [])
    attorneyNames = data.get('attorneyNames', [])
    
    # Construct the prompt for OpenAI
    prompt = "Match the following attorney names to their corresponding emails:\n\n"
    prompt += "Attorney Names:\n" + "\n".join(attorneyNames) + "\n\n"
    prompt += "Emails:\n" + "\n".join(emails) + "\n\n"
    prompt += "In Json, Provide the matches as a list of objects, each containing 'name' and 'email' as keys. In the name value just return the first name."
    
    try:
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            response_format={"type": "json_object"}
        )
        
        # Assuming the response is a JSON string that needs to be converted into a Python object
        matches = eval(response.choices[0].message.content)
        
        # Return the matched names and emails as JSON
        return jsonify(matches)
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An error occurred while processing your request'}), 500
    
# The extract_attorneys_from_domain function is designed to automate the process of extracting attorney names from a given domain. It performs several steps to achieve this:
# 1. It scrapes navigation links from the provided domain name to identify potential pages that might list attorney names.
# 2. It then processes these links to find a specific link that is most likely to contain attorney names, often labeled as something like 'Our Attorneys', 'Meet the Team', or similar.
# 3. Once the specific link is identified, the function fetches the content of that page.
# 4. The content is then passed to an AI model, which extracts the names of the attorneys from the page content.
# 5. Finally, the extracted names are returned in a JSON format to the caller.
# This function is useful for automating the collection of attorney names from law firm websites without manual browsing and data entry, streamlining data collection processes for various applications.

@app.route("/extract_attorneys_from_domain/<domain_name>", methods=['GET'])
def extract_attorneys_from_domain(domain_name):
    print(f"Starting to process domain: {domain_name}")
    try:
        # Step 1: Scrape navigation links
        navigation_links = scrape_links(domain_name)
        if not navigation_links:
            print(f"Failed to scrape navigation links for {domain_name}.")
            return jsonify({'error': 'Failed to scrape navigation links'}), 500

        # Step 2: Find specific link for attorneys
        nav_links_response = find_nav_links(navigation_links)
        if not nav_links_response:
            print(f"Failed to find specific links for {domain_name}.")
            return jsonify({'error': 'Failed to find specific links'}), 500

        # Convert nav_links_response from JSON string to Python dictionary
        nav_links_response_dict = json.loads(nav_links_response)
        lawyer_link_url = nav_links_response_dict.get("lawyer link")
        all_nav_links = nav_links_response_dict.get("all nav links", [])  # Extract 'all nav links' information
        
        if not lawyer_link_url:
            print(f"No lawyer link found for {domain_name}.")
            return jsonify({'error': 'No lawyer link found'}), 404

        # Step 3: Extract attorney names
        attorney_names = extract_attorney_names(lawyer_link_url)
        if not attorney_names:
            print(f"No attorney names found for {domain_name}.")
            return jsonify({'error': 'No attorney names found'}), 404

        # Assuming attorney_names is already in JSON format
        return jsonify({'attorney_names': attorney_names, 'all_nav_links': all_nav_links})
    except Exception as e:
        print(f"An unexpected error occurred while processing {domain_name}: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
    # @app.route("/process_domain/<domain_name>", methods=['GET'])
    # def process_domain(domain_name):
    #     print(f"Starting to process domain: {domain_name}")
    #     try:
    #         print("Scraping navigation links...")
    #         navigation_links = scrape_links(domain_name)
    #         if not navigation_links:  # Check if navigation_links is empty
    #             print(f"Skipping {domain_name} due to an error in scraping links.")
    #             return [], ""

    #         print("Finding specific links...")
    #         nav_links = find_specific_links(navigation_links)
    #         if not nav_links:  # Check if nav_links is empty or an error occurred
    #             print(f"Skipping {domain_name} due to an error in finding specific links.")
    #             return [], ""

    #         print("Converting navigation links from string to JSON...")
    #         nav_links_json = json.loads(nav_links)  # Convert string to JSON

    #         print("Extracting lawyer link URL...")
    #         lawyer_link_url = nav_links_json.get("lawyer link")
    #         if not lawyer_link_url:  # Check if lawyer_link_url is empty
    #             print(f"No lawyer link found for {domain_name}. Skipping.")
    #             return [], ""

    #         print(f"Extracting attorney names from: {lawyer_link_url}")
    #         attorney_names = extract_attorney_names(lawyer_link_url)
    #         if not attorney_names:  # Check if attorney_names is empty
    #             print(f"No attorney names found for {domain_name}. Skipping.")
    #             return [], ""

    #         print("Compiling list of links...")
    #         links = [link for link in nav_links_json.get('links', [])]

    #         print(f"Finished processing {domain_name}.")
    #         return links, attorney_names
    #     except Exception as e:
    #         print(f"An unexpected error occurred while processing {domain_name}: {e}")
    #         return [], ""


if __name__ == "__main__":
    app.run(debug=True)
    # test_domain = "https://sptaxlaw.com"
    # links, attorney_names = process_domain(test_domain)
    # print("Links:", links)
    # print("Attorney Names:", attorney_names)