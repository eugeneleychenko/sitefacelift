from langchain.document_loaders import BSHTMLLoader
from langchain.chat_models import ChatOpenAI
#from langchain.schema import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain.schema.messages import SystemMessage
from dotenv import load_dotenv
#from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import HTMLHeaderTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
import requests
import openai
import csv
import json
import os


load_dotenv()

def ask_questions_to_website(urls):
    html_docs = []
    for url in urls:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        html = response.text
        html_docs.append(html)
    
# Then load all the HTML documents using BSHTMLLoader
    loaders = [BSHTMLLoader(doc) for doc in html_docs]
    docs = [loader.load() for loader in loaders]
    page_contents = []
    for doc in docs:
        for item in doc:
            page_contents.append(item.page_content)

    all_page_content = " ".join(page_contents)
    print(all_page_content)

    # Initialize the QAGenerationChain
    # model = ChatOpenAI(temperature=0, model="gpt-4-1106-preview")
    # model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-1106")
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
            
           here is an example of an output: "detailsData": "{\n    \"title\": \"Nationwide Resources\",\n    \"content\": \"The Cochran Firm has offices nationwide with a team of experienced and aggressive personal injury attorneys and criminal defense lawyers. They offer tireless and effective legal representation across the country.\"\n  },\n  {\n    \"title\": \"Diverse Specializations\",\n    \"content\": \"Attorneys at The Cochran Firm specialize in a variety of practice areas including personal injury, civil rights, medical malpractice, and employment discrimination. This allows them to handle a wide range of cases with expert knowledge.\"\n  },\n  {\n    \"title\": \"Legacy of Excellence\",\n    \"content\": \"Founded by legendary attorney Johnnie L. Cochran, Jr., The Cochran Firm continues his mission of providing justice to the wronged and giving a voice to the silenced. They are committed to restoring justice and advocating for individual rights.\"\n  }",
        
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
    # questions =  "return the CTA which usually phrases like 'to call or text the contact number for a consultation'.",

    # Split the all_page_content
    html_header_splitter = HTMLHeaderTextSplitter(headers_to_split_on=[("h1", "Main Heading"), ("h2", "Subheading")])
    html_header_splits = html_header_splitter.split_text(all_page_content)

    # Define our text splitter
    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150)
    # all_splits = text_splitter.split_documents(html_header_splits)

    # Embed the splits
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_texts(html_header_splits, embeddings)

    # Build a QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-4-1106-preview", temperature=0),
        chain_type="stuff",
        retriever=vectordb.as_retriever(),
    )

    # Ask a question!
    results = []
    for i, question in enumerate(questions):
        chat_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=all_page_content),
                HumanMessagePromptTemplate.from_template("""Only respond with the answer. No full sentences.
                                                         If it doesn't exists, return null. 
                                                          {text}"""),
            ]
        )
        qa = qa_chain.run(chat_template.format_messages(text=question))
        results.append((question, qa.content, questionsArr[i]))
        print(f"Question: {question}\nAnswer: {qa.content}\n")
    # Create a CSV file with the questions and answers
    with open('qa_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Question', 'Answer', 'QuestionArr'])
        for i, result in enumerate(results):
            writer.writerow([result[0], result[1], result[2]])

# Create a JSON file with the questions and answers
    
    
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

# # Use the function
urls = [ 'https://www.newyorkcitydiscriminationlawyer.com/', 'https://www.newyorkcitydiscriminationlawyer.com/team/', 'https://www.newyorkcitydiscriminationlawyer.com/testimonials/']
ask_questions_to_website(urls)
