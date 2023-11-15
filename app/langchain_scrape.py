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

load_dotenv()

def ask_questions_to_website(url):
    # print(openai.__file__)
    # Load the website content
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    html = response.text

    # Create an html2text.HTML2Text object and override some properties
    h = html2text.HTML2Text()
    h.ignore_links = False

    # Convert the HTML to Markdown
    markdown = h.handle(html)
    # print(markdown)
    
    def save_markdown_to_file(markdown, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(markdown)

# Save the markdown content to a file
    save_markdown_to_file(markdown, 'site.md')

# Then load the markdown file
    loader = TextLoader('site.md')
    doc = loader.load()[0]
    # print(doc.page_content)

    # Initialize the QAGenerationChain
    model = ChatOpenAI(temperature=0, model="gpt-4-1106-preview")
    
    # Define the questions
    questions = [
        "return the CTA which usually phrases like 'to call or text the contact number for a consultation'.",
        "Find 3 advantages that sets this firm apart.",
        "what is the address of this firm?",
        "What is the phone number of this firm?",
        "What is the contact email of this firm?",
        "In an array, return the navigation items of this site.",
        "What is the name of this company?",
        "What is the subheading of this company?",
        "Near the top of the site, there will a paragraph description about this firm, return it.",
        "What is the CTA close to the top of the site?",
        "Return 9 practice areas of this law firm, in an array.",
        "Return, in an array of objects, 4 names of lawyers and their titles.",
        "What is the firm open?",
        "What is the phone number of this firm?",
        "Return 3 testimonials from this site.",
        "Return 9 practice areas of this law firm, in an array."
    ]
    # questions =  "return the CTA which usually phrases like 'to call or text the contact number for a consultation'.",

    # Run the chain for each question and print the results
    for question in questions:
        chat_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=doc.page_content),
                HumanMessagePromptTemplate.from_template("Only respond with the answer. No full sentences. {text}"),
            ]
        )
        qa = model(chat_template.format_messages(text=question))
        print(f"Question: {question}\nAnswer: {qa.content}\n")
        
   

# # Use the function
ask_questions_to_website('https://gio-law.com/')
