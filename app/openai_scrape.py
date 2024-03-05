from langchain.document_loaders import TextLoader
from dotenv import load_dotenv
import html2text
import requests
from openai import OpenAI
import csv
import json
import os
import re



load_dotenv()

def clean_text(text):
    # This regex matches any non-printable ASCII characters and non-ASCII characters
    cleaned_text = re.sub(r'[^\x20-\x7E]+', '', text)
    return cleaned_text

def ask_questions_to_website(urls):
    markdown_files = []
    for url in urls:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'  # Set encoding to UTF-8
        html = response.text

        start_index = html.find("Simplify Your Case")
        end_index = html.find("Privacy Policy")
        if start_index != -1 and end_index != -1:
            # Slice the HTML from "Simplify Your Case" up to "terms of use"
            html = html[start_index:end_index]
        elif start_index != -1:
            # Slice the HTML from "Simplify Your Case" onwards if "terms of use" is not found
            html = html[start_index:]
        
        h = html2text.HTML2Text()
        h.ignore_links = True  # Set to True to ignore links
        h.ignore_images = True
        h.body_width = 0
        markdown = h.handle(html)

        # Clean the markdown text to remove strange characters
        markdown = clean_text(markdown)

        def save_markdown_to_file(markdown, filename):
            os.makedirs('markdown', exist_ok=True)
            with open(os.path.join('markdown', filename), 'w', encoding='utf-8') as f:
                f.write(markdown)
            return os.path.join('markdown', filename)

        markdown_file = save_markdown_to_file(markdown, f'{url.replace("/", "_")}.md')
        markdown_files.append(markdown_file)

# Then load all the markdown files
    loaders = [TextLoader(file) for file in markdown_files]
    docs = [loader.load() for loader in loaders]
    page_contents = []
    for doc in docs:
        for item in doc:
            page_contents.append(item.page_content)

    all_page_content = " ".join(page_contents)
    print(all_page_content)

    # Initialize the QAGenerationChain
    # model = ChatOpenAI(temperature=0, model="gpt-4-1106-preview")
    client = OpenAI()
    
    
   
    # Define the questions
    questionsArr = [
                    "paragraph","detailsData", "address", 
                    "phoneNumber", "email", "linkNames", 
                    "companyName", "subHeading", "valueProp", "CTA",
                    "topics", "members", "openHours", "testimonalData"
                    
                    ]
    questions = [
        "return the CTA which usually phrases like 'to call or text the contact number for a consultation'.",
        """
        " Find 3 advantages that sets this firm apart. organize the objects in this way {
            "title": 3-4 word title of the advantage,
            "content": 2 sentences talking about the advantage.
            }
            
           Here is an example of an output. Focus on the format, not the content: 
           
           {\n    \"title\": \"Decades of Experience\",\n    \"content\": \"The attorneys at Venardi Zurada have over 35 years of experience serving Northern California. Their extensive tenure in the legal field showcases their deep knowledge and expertise in handling a wide range of cases.\"\n  },\n  {\n    \"title\": \"Big Firm Experience, Boutique Attention\",\n    \"content\": \"The attorneys at Venardi Zurada combine big firm experience with boutique office attention. This unique approach allows them to provide individualized and attentive representation to each client, ensuring personalized service and care.\"\n  },\n  {\n    \"title\": \"Respected by Opposing Counsel\",\n    \"content\": \"Venardi Zurada is respected by opposing counsel, feared by insurance companies, and followed by jurors. Their reputation in the legal community demonstrates their ability to effectively advocate for their clients and achieve successful outcomes.\"\n  }"
           
        
        """,
        "What is the address of this firm?",
        "What is the phone number of this firm?",
        "What is the contact email of this firm?",
        """
        In an array, return in UPPERCASE the navigation items of this site. If the markdown contains several levels, only return the highest level. Format it like this. only focus on format, not content [
    "Home",
    "Our Firm",
    "Our Team",
    "Practice Areas",
    "Publications & Seminars",
    "Contact",
    "Office"
  ],
  """ ,
        "What is the name of this company?",
        "What is the subheading of this company?",
        "Near the top of the site, there will a paragraph description about this firm, return it. If it doesn't exist, write 2 paragraphs about this firm",
        "What is the CTA close to the top of the site?",
        "Return 9 practice areas of this law firm, in an array.",
        """
        ( Return, in an array of objects, 4 names of lawyers and their titles. For example 
        
        ```json\n[\n  {\n    \"name\": \"Mark Venardi\",\n    \"position\": \"Partner\"\n  },\n  {\n    \"name\": \"Martin Zurada\",\n    \"position\": \"Partner\"\n  },\n  {\n    \"name\": \"Terry Buller\",\n    \"position\": \"Of Counsel\"\n  },\n  {\n    \"name\": \"Mark Freeman\",\n    \"position\": \"Senior Trial Attorney\"\n  }\n]\n```
        
        """,
        " When is the firm open?",
        
        """
          Return 3 testimonials from this site. They should be in an array of objects, including text, author, location. For example 
          
          "```json\n[\n    {\n        \"text\": \"Matt is my go to lawyer. He has been there for me and so many of my teammates over the years.\",\n        \"author\": \"Dwight Gooden\",\n        \"location\": null\n    },\n    {\n        \"text\": \"Matt is a strategic thinker and really knows how to analyze and formulate a litigation game plan.\",\n        \"author\": \"Phil Regan\",\n        \"location\": null\n    },\n    {\n        \"text\": \"I heard other players saying amazing things about Matt and now I know for myself that it's all true as he never quits until the catch is made!\",\n        \"author\": \"Endy Chavez, NY Mets Player\",\n        \"location\": null\n    }\n]\n```"
        """
    ]
    # questions =  "return the CTA which usually phrases like 'to call or text the contact number for a consultation'.",

    # Run the chain for each question and print the results
    results = []
    for i, question in enumerate(questions):
        # Create the messages for the chat completion
        messages = [
            {"role": "system", "content": all_page_content},
            {"role": "user", "content": f"Only respond with json with the answer. No full sentences. If it doesn't exist, return null. Not the string null, but the value null. {question}"}
        ]
        
        # Get the completion from the OpenAI chat model
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0,
            response_format={"type": "json_object"}
        )
        
        # Extract the content from the completion
        # Assuming the last message is the response from the model
        answer_content = json.loads(completion.choices[0].message.content) if completion.choices else None
        
        # Append the result as a JSON object
        results.append({
            "question": question,
            "answer": answer_content,
            "questionArr": questionsArr[i]
        })

    # Print the results
    for result in results:
        print(f"Question: {result['question']}\nAnswer: {result['answer']}\n")
        
    # Create a CSV file with the questions and answers
    with open('qa_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Question', 'Answer', 'QuestionArr'])
        for i, result in enumerate(results):
            writer.writerow([result[0], result[1], result[2]])

# Create a JSON file with the questions and answers
    
    
    if 'www.' not in url:
        url = url.replace('https://', 'https://www.')
        url = url.replace('http://', 'http://www.')
    domain = url.split('www.')[-1]
    if '.com' in domain:
        company_name = domain.split('.com')[0] + '.com'
    elif '.net' in domain:
        company_name = domain.split('.net')[0] + '.net'
    elif '.org' in domain:
        company_name = domain.split('.org')[0] + '.org'
    directory = f'/Users/eugeneleychenko/Downloads/sfl/sitefacelift/src/data/{company_name}'
    os.makedirs(directory, exist_ok=True)
    with open(f'{directory}/data.json', 'w', encoding='utf-8') as jsonfile:
        json_results = {}
        for q, (_, a, _) in zip(questionsArr, results):
            if isinstance(a, str) and (a.startswith('{') or a.startswith('[')):
                try:
                    a = json.loads(a.replace('}{', '},{'))
                except json.JSONDecodeError:
                    pass
            json_results[q] = a
        json.dump(json_results, jsonfile, indent=4)

# # Use the function
urls = [  "https://richardburtlaw.com/", "https://richardburtlaw.com/richard-burt-bio/", "https://richardburtlaw.com/contact/"]
ask_questions_to_website(urls)
