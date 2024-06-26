import requests
import html2text
import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from requests.exceptions import ConnectionError

load_dotenv()

# Function to clean and convert HTML to markdown
def clean_and_convert_to_markdown(html):
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    h.body_width = 0
    markdown = h.handle(html)
    return markdown

# Function to save markdown content to a file
def save_markdown_to_file(markdown, filename):
    os.makedirs('markdown', exist_ok=True)
    filepath = os.path.join('markdown', filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown)
    return filepath

# Function to scrape websites and convert pages to markdown
def scrape_and_convert(urls):
    markdown_files = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    for url in urls:
        retries = 0
        max_retries = 3
        while retries < max_retries:
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    html = response.text
                    markdown = clean_and_convert_to_markdown(html)
                    filename = url.replace("http://", "").replace("https://", "").replace("/", "_") + ".md"
                    markdown_file = save_markdown_to_file(markdown, filename)
                    markdown_files.append(markdown_file)
                    break  # Exit the retry loop if successful
                else:
                    print(f"Failed to fetch {url} with status code {response.status_code}")
                    break  # Exit the retry loop if response code is not 200
            except ConnectionError as e:
                print(f"Connection error on attempt {retries+1} for {url}: {e}")
                retries += 1
                if retries >= max_retries:
                    print("Max retries reached. Giving up on " + url)
                    break  # Exit the retry loop if max retries reached
    return markdown_files

# Function to combine markdown files into one
def combine_markdown_files(files):
    combined_content = ""
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            combined_content += f.read() + "\n\n"
    return combined_content

# Function to ask questions using OpenAI and return JSON answers
def ask_questions_with_openai(markdown_content, questions):
    client = OpenAI()  # Initialize the OpenAI client
    # Construct the message with all questions
    questions_content = "\n\n".join([f"Q: {q}" for q in questions])
    messages = [
        {"role": "system", "content": markdown_content},
        {"role": "user", "content": f"Only respond with json with the answer to the following questions. If it doesn't exist, return null. Not the string null, but the value null.\n\n{questions_content}"}
    ]
    completion = client.chat.completions.create(
        # model="gpt-3.5-turbo-0125",
        model = os.getenv("latest_openai_model"),
        messages=messages,
        temperature=0,
        response_format={"type": "json_object"}
    )
    
    if completion.choices:
        answers_dict = json.loads(completion.choices[0].message.content)
        print(answers_dict)
    else:
        print("No choices in the response.")
        
    # Process the response to restructure it
    # structured_response = process_response(answers_dict)
    return answers_dict

def process_response(response):
    structured_response = {}

    # Extract and rename 'CTA' to 'paragraph'
    # if 'CTA' in response:
    #     structured_response['paragraph'] = response['CTA']

    # # Process 'advantages' and rename to 'detailsData'
    # if 'advantages' in response and isinstance(response['advantages'], list):
    #     structured_response['detailsData'] = response['advantages']

    
    return structured_response

# Main function to execute the app logic
def main(urls=None):
    if urls is None:
        urls = ["https://integratedgeneralcounsel.com/","https://integratedgeneralcounsel.com/about-us/"," https://integratedgeneralcounsel.com/services/"," https://integratedgeneralcounsel.com/what-clients-say/"]
    questions = [
        "return the CTA which usually phrases like 'to call or text the contact number for a consultation'. If none exist, use 'Contact Us Today'. Name the key 'paragraph' ",
        """
        Find 4 advantages that sets this firm apart. Organize the objects in this way {
            "title": 3-4 word title of the advantage,
            "content": 2 sentences talking about each advantage.
        }.
        Name the key 'detailsData'.
        """,
         "What is the address of this firm?. Name this key 'address' ",
        "What is the phone number of this firm?  Name this key 'phoneNumber' ",
        "What is the contact email of this firm? Name this key 'email' ",
        """
        In an array, return in UPPERCASE the navigation items of this site. If the markdown contains several levels, only return the highest level. Format it like this. only focus on format, not content [
    "Home",
    "Our Firm",
    "Our Team",
    "Practice Areas",
    "Publications & Seminars",
    "Contact",
    "Office"
  ]
  Name this key 'linkNames' 
  ,
  """ ,
        "What is the name of this company? Name this key 'companyName'. Make sure it's at most 5 words.",
        "What is the subheading of this company? Name this key 'subHeading' ",
        "Near the top of the site, there will a paragraph description about this firm, return it. If it doesn't exist, write 2 paragraphs about this firm. Name this key 'valueProp' ",
        "What is the CTA close to the top of the site? Name this key 'CTA' ",
        "Return 9 practice areas of this law firm, in an array. Dont return an null. Name this key 'topics' ",
        """
        ( Return, in an array of objects, 4 names of lawyers and their titles. Don't make up any lawyers. If less than 4 exists, then show only the real ones. For example 
        
        ```json\n[\n  {\n    \"name\": \"Mark Venardi\",\n    \"position\": \"Partner\"\n  },\n  {\n    \"name\": \"Martin Zurada\",\n    \"position\": \"Partner\"\n  },\n  {\n    \"name\": \"Terry Buller\",\n    \"position\": \"Of Counsel\"\n  },\n  {\n    \"name\": \"Mark Freeman\",\n    \"position\": \"Senior Trial Attorney\"\n  }\n]\n```
        
         Name this key 'members' 
        """,
        " When is the firm open? Respond on one line, never as with multiple keys. Name this key 'openHours' " ,
        
        """
          Return 3 testimonials from this site. Each should not be longer than 50 words. They should be in an array of objects, including text, author, location. For example 
          
          "```json\n[\n    {\n        \"text\": \"Matt is my go to lawyer. He has been there for me and so many of my teammates over the years.\",\n        \"author\": \"Dwight Gooden\",\n        \"location\": null\n    },\n    {\n        \"text\": \"Matt is a strategic thinker and really knows how to analyze and formulate a litigation game plan.\",\n        \"author\": \"Phil Regan\",\n        \"location\": null\n    },\n    {\n        \"text\": \"I heard other players saying amazing things about Matt and now I know for myself that it's all true as he never quits until the catch is made!\",\n        \"author\": \"Endy Chavez, NY Mets Player\",\n        \"location\": null\n    }\n]\n```"
        If none exist, make them up.
        Name this key 'testimonalData' 
        """
    ]
    markdown_files = scrape_and_convert(urls)
    combined_markdown = combine_markdown_files(markdown_files)
    
    # Ask all questions at once
    answers = ask_questions_with_openai(combined_markdown, questions)
    
    # Assuming answers is structured correctly, you can directly print or save it
    print("Processed Answers:", answers)
    print(json.dumps(answers, indent=4))
    
    url = urls[0]  # Assuming you want to use the first URL for naming
    if 'www.' not in url:
        url = url.replace('https://', 'https://www.')
        url = url.replace('http://', 'http://www.')
    domain = url.split('www.')[-1]
    if '.com' in domain:
        company_name = domain.split('.com')[0] + '.com'
    elif '.net' in domain:
        company_name = domain.split('.net')[0] + '.net'
    elif '.law' in domain:
        company_name = domain.split('.law')[0] + '.law'
    elif '.org' in domain:
        company_name = domain.split('.org')[0] + '.org'
    elif '.io' in domain:
        company_name = domain.split('.io')[0] + '.io'    
    elif '.legal' in domain:  # Add this condition to handle .legal domains
        company_name = domain.split('.legal')[0] + '.legal'
    elif '.la' in domain:  # Add this condition to handle .legal domains
        company_name = domain.split('.la')[0] + '.la'    
    directory = f'/Users/eugeneleychenko/Downloads/sfl/sitefacelift/src/data/{company_name}'
    os.makedirs(directory, exist_ok=True)
    with open(f'{directory}/data.json', 'w', encoding='utf-8') as jsonfile:
        json_results = answers  # Assuming json_results is your structured JSON data
        # Populate json_results with your data here
        json.dump(json_results, jsonfile, indent=4)
    
if __name__ == "__main__":
    main()
