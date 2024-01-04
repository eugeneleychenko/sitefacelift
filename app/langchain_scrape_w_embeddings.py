from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain.schema.messages import SystemMessage
from langchain.embeddings import OpenAIEmbeddings
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
        response = requests.get(url, headers=headers)
        html = response.text

        h = html2text.HTML2Text()
        h.ignore_links = True
        markdown = h.handle(html)

        def save_markdown_to_file(markdown, filename):
            os.makedirs('markdown', exist_ok=True)
            with open(os.path.join('markdown', filename), 'w', encoding='utf-8') as f:
                f.write(markdown)
            return os.path.join('markdown', filename)

        markdown_file = save_markdown_to_file(markdown, f'{url.replace("/", "_")}.md')
        markdown_files.append(markdown_file)

    # Load all the markdown files into the vectorstore using OpenAI embeddings
    embeddings = OpenAIEmbeddings()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    # Initialize FAISS vectorstore with required arguments

    for markdown_file in markdown_files:
        loader = TextLoader(markdown_file)
        documents = loader.load()
        docs = text_splitter.split_documents(documents)
        vectorstore = FAISS.from_documents(docs, embeddings)
        docs = text_splitter.split_documents(documents)
        vectorstore.add_documents(docs)

    # Initialize the ChatOpenAI model
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
        " Find 3 advantages that sets this firm apart. organize the objects in this way {
            "title": 3-4 word title of the advantage,
            "content": 2 sentences talking about the advantage.
            }
            
           here is an example of an output: {\n    \"title\": \"Nationwide Resources\",\n    \"content\": \"The Cochran Firm has offices nationwide with a team of experienced and aggressive personal injury attorneys and criminal defense lawyers. They offer tireless and effective legal representation across the country.\"\n  },\n  {\n    \"title\": \"Diverse Specializations\",\n    \"content\": \"Attorneys at The Cochran Firm specialize in a variety of practice areas including personal injury, civil rights, medical malpractice, and employment discrimination. This allows them to handle a wide range of cases with expert knowledge.\"\n  },\n  {\n    \"title\": \"Legacy of Excellence\",\n    \"content\": \"Founded by legendary attorney Johnnie L. Cochran, Jr., The Cochran Firm continues his mission of providing justice to the wronged and giving a voice to the silenced. They are committed to restoring justice and advocating for individual rights.\"\n  }
        
        """,
        "What is the address of this firm?",
        "What is the phone number of this firm?",
        "What is the contact email of this firm?",
        "In an array, return in UPPERCASE the navigation items of this site. If the markdown contains several levels, only return the highest level.",
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

    # Run the chain for each question and print the results
    results = []
    for i, question in enumerate(questions):
        chat_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=vectorstore),
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
    company_name = url.split('www.')[-1].split('.com')[0] + '.com'
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

# Use the function
urls = [ 'https://www.cashdankane.com/', "https://www.cashdankane.com/attorneys/", "https://www.cashdankane.com/practice-areas/labor-and-employment/"]
ask_questions_to_website(urls)
