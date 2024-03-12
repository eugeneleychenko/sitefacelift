import requests
import csv
import json
from dotenv import load_dotenv, dotenv_values
import re
from bs4 import BeautifulSoup
from openai import OpenAI
import html2text

load_dotenv()
config = dotenv_values(".env")

domain_name = "http://petersonprice.com/"

def get_snov_token():
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
        return token_data.get('access_token')
    else:
        print(f"Failed to obtain token, status code: {response.status_code}")
        return None

def domain_search(domain):
    token = get_snov_token()
    params = {
        'access_token': token,
        'domain': domain,
        'type': 'all',
        'limit': 10,
        'lastId': 0,
        # 'positions[]': ['Software Developer','QA']
    }

    res = requests.get('https://api.snov.io/v2/domain-emails-with-info', params=params)

    return json.loads(res.text)

def scrape_links(domain_name):
    """
    Function to scrape the given domain name, convert the page into markdown, and find the links in the navigation.
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
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

def find_specific_links(navigation_links):
    """
    Takes in an array of navigation links and uses OpenAI to determine which link likely contains the list of attorneys/people working at the firm,
    the link to practice areas, and the link to about us.
    """
    client = OpenAI()
    system_message = """
             I am looking for links in a site's navigation. I will provide a list of links from the top to the bottom of the site. Weigh the links at the beginning higher than ones at the bottom of the list. Given a list of website navigation links, identify the link (keep in mind that i'm providing the full link, but in my examples im only providing the subdirectory) that most likely contains the list of attorneys or people working at the firm (this usually looks like /attorney, /people, or /who-we-are), the link to practice areas (this usually looks like /practice-areas or /what-we-do),the link to about us (usually looks like /about-us), and links to testimonials (usually look like /testimonials). Here are the links:
             
             Which link contains the list of attorneys? Which link leads to practice areas? Which link leads to about us? Which link leads to testimonials?
             
             Only return a json with two keys, 
             1) call this key, 'links' and have an array of the links that are in the navigation, and 2) call this 'lawyer link' the link for the url that contains the list of lawyers that work at the firm. The links should be full links, including the domain. Do not make up any links, only use it from the list provided. If links for certain pages dont exist then ignore that page.
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

def extract_attorney_names(attorney_page_url):
    """
    Takes a URL that contains the names of the attorneys that work at the firm,
    converts that page to markdown, passes it to OpenAI, and extracts all the names
    of the people who work at the firm.
    """
    try:
        # Fetch the HTML content from the URL
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        response = requests.get(attorney_page_url, headers=headers)
        if response.status_code == 200:
            # Convert HTML to Markdown
            markdown = html2text.HTML2Text().handle(response.text)
            client = OpenAI()
            # Construct the prompt to extract names
            prompt = "Extract all the names of the people who work at the firm from the following text:\n\n" + markdown
            # Pass the prompt to the LLM
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0
            )
            # Extract and return the names from the response
            names = response.choices[0].message.content
            return names
        else:
            print(f"Failed to fetch {attorney_page_url} with status code {response.status_code}")
            return []
    except Exception as e:
        print(f"An error occurred while processing {attorney_page_url}: {e}")
        return []


def process_domain(domain_name):
    try:
        navigation_links = scrape_links(domain_name)
        if not navigation_links:  # Check if navigation_links is empty
            print(f"Skipping {domain_name} due to an error.")
            return [], ""

        nav_links = find_specific_links(navigation_links)
        if not nav_links:  # Check if nav_links is empty or an error occurred
            print(f"Skipping {domain_name} due to an error in finding specific links.")
            return [], ""

        nav_links_json = json.loads(nav_links)  # Convert string to JSON

        lawyer_link_url = nav_links_json.get("lawyer link")
        if not lawyer_link_url:  # Check if lawyer_link_url is empty
            print(f"No lawyer link found for {domain_name}. Skipping.")
            return [], ""

        attorney_names = extract_attorney_names(lawyer_link_url)
        if not attorney_names:  # Check if attorney_names is empty
            print(f"No attorney names found for {domain_name}. Skipping.")
            return [], ""

        links = [link for link in nav_links_json.get('links', [])]

        return links, attorney_names
    except Exception as e:
        print(f"An unexpected error occurred while processing {domain_name}: {e}")
        return [], ""

def read_and_process_csv(input_csv_path, output_csv_path):
    with open(input_csv_path, mode='r', encoding='utf-8') as infile, \
         open(output_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Write the header for the output CSV
        writer.writerow(['Domain Name', 'Links', 'Attorney Names'])

        # Skip the header row from the input CSV if it exists
        next(reader, None)

        for row in reader:
            domain_name = row[0]
            links, attorney_names = process_domain(domain_name)
            # Convert list of links and attorney names to a string representation
            links_str = '; '.join(links)
            attorney_names_str = attorney_names.replace('\n', '; ')
            writer.writerow([domain_name, links_str, attorney_names_str])

# Example usage
input_csv_path = 'input_domains.csv'
output_csv_path = 'processed_domains.csv'
read_and_process_csv(input_csv_path, output_csv_path)