from langchain.document_loaders import TextLoader
from langchain.chat_models import ChatOpenAI
# from langchain.schema import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain.schema.messages import SystemMessage
from dotenv import load_dotenv
import html2text
import requests
import openai
import csv
import json
import os



load_dotenv()

def ask_questions_to_website(urls):
    markdown_files = []
    for url in urls:
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        response = requests.get(url, headers=headers, verify=False)
        html = response.text

        h = html2text.HTML2Text()
        h.ignore_links = True  # Set to True to ignore links
        markdown = h.handle(html)

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
    model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-1106")
    # model=AzureChatOpenAI(temperature=0, deployment_name=os.getenv("OPENAI_DEPLOYMENT_NAME"), openai_api_version="2023-05-15" )
   
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
            
           Here is an example of an output. Focus on the format, not the content: {\n    \"title\": \"Elite Legal Background\",\n    \"content\": \"The lead attorneys at Clayton Trial Lawyers come from 'Big Law' representing corporations, insurance companies, and high net worth individuals. This elite legal background sets them apart from other personal injury law firms or litigation boutiques.\"\n  },\n  {\n    \"title\": \"High Value & Expertise\",\n    \"content\": \"Clayton Trial Lawyers deliver high value and expertise, personalized to each client's needs. Their experience and determination have earned their clients over $150 million in jury verdicts.\"\n  },\n  {\n    \"title\": \"Listed as 'Best Lawyers, Best Law Firms'\",\n    \"content\": \"Clayton Trial Lawyers was listed as 'Best Lawyers, Best Law Firms' and No. 1 in the region, according to U.S. News & World Report. This recognition showcases their commitment to excellence and success in the legal field.\"\n  }"
           
        
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
        "Near the top of the site, there will a paragraph description about this firm, return it.",
        "What is the CTA close to the top of the site?",
        "Return 9 practice areas of this law firm, in an array.",
        """
        ( Return, in an array of objects, 4 names of lawyers and their titles. For example [
            {
                name: "Carmen 'Jack' Giordano, Esq.",
                position: "Principal Attorney",
            },
            {
                name: "Stefanie Behler Soriano, Esq.",
                position: "Associate Attorney",
            }]
        
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
        chat_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=all_page_content),
                HumanMessagePromptTemplate.from_template("""Only respond with the answer. No full sentences.
                                                         If it doesn't exists, return null. Not the string null, but the value null. 
                                                         
                                                          {text}"""),
            ]
        )
        qa = model(chat_template.format_messages(text=question))
        results.append((question, qa.content, questionsArr[i]))
        print(f"Question: {question}\nAnswer: {qa.content}\n")
        
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
urls = [ 'https://www.hillbetts.com/', "https://www.hillbetts.com/attorneys", "https://www.hillbetts.com/practice-areas"]
ask_questions_to_website(urls)
