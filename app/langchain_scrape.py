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
    questionsArr = [
                    "paragraph","detailsData", "address", 
                    "phoneNumber", "email", "linkNames", 
                    "companyName", "subHeading", "valueProp", "CTA",
                    "topics", "members", "openHours", "testimonalData"
                    
                    ]
    questions = [
        "return the CTA which usually phrases like 'to call or text the contact number for a consultation'.",
        """
        " Find 3 advantages that sets this firm apart. organize it in this way {
            "title": 3-4 word title of the advantage,
            "content": 2 sentences talking about the advantage.
            }
        
        """,
        "What is the address of this firm?",
        "What is the phone number of this firm?",
        "What is the contact email of this firm?",
        "In an array, return in UPPERCASE the navigation items of this site.",
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
          Return 3 testimonials from this site. They should be in an array of objects, including text, author, location. For example ""[
            {
                text: "Carmen was absolutely wonderful to work with. He was truly honest and I never felt taken advantage of. I can't recommend this law office and Carmen enough.",
                author: "Jaime Oliver",
                location: "New York",
            },
            {
                text: "Even after the case we still keep in contact for any question that we still might have, for people who do not speak English I recommend him, he makes sure that the person in the case understands everything that happens in their case.",
                author: "Atriz R",
                location: "Manhattan, New York",
            }]"
        """
    ]
    # questions =  "return the CTA which usually phrases like 'to call or text the contact number for a consultation'.",

    # Run the chain for each question and print the results
    results = []
    for i, question in enumerate(questions):
        chat_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=doc.page_content),
                HumanMessagePromptTemplate.from_template("""Only respond with the answer. No full sentences.
                                                         If it doesn't exists say 'N/A'. 
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
    with open('/Users/eugeneleychenko/Downloads/sfl/sitefacelift/src/data1.json', 'w', encoding='utf-8') as jsonfile:
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
ask_questions_to_website('https://gio-law.com/')
