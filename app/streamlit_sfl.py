import streamlit as st
import requests
from bs4 import BeautifulSoup
import re
from dotenv import load_dotenv, dotenv_values
import json
import os
from new_openai_scrape import scrape_and_convert, ask_questions_with_openai, combine_markdown_files

load_dotenv()
config = dotenv_values(".env")

# Snov.io integration
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

def ping_snov(domain):
    token = get_snov_token()
    if not token:
        print("Failed to obtain Snov.io access token.")
        return []
    
    params = {
        'access_token': token,
        'domain': domain,
        'type': 'all',
        'limit': 10,
        'lastId': 0,
    }

    response = requests.get('https://api.snov.io/v2/domain-emails-with-info', params=params)
    if response.status_code == 200

# Function to extract attorney names from a website
def extract_attorney_names(url):
   response = requests.get(url)
   soup = BeautifulSoup(response.content, 'html.parser')
   
   # Implement logic to find the link containing attorney names
   # and extract the names from that page
   # Return a list of attorney names
   pass

# Matching attorney emails
def match_attorney_emails(attorney_names, snov_emails):
   # Implement logic to match attorney names with emails from Snov.io
   # Return a list of matched (name, email) tuples
   pass

def main():
   st.title("Landing Page Generator")
   
   # Upload a file or provide a URL for lead sources
   upload_method = st.radio("Select input method", ["Upload File", "Enter URL"])
   
   if upload_method == "Upload File":
       uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv"])
       if uploaded_file is not None:
           # Process the uploaded file
           pass
   else:
       url = st.text_input("Enter the URL containing lead sources")
       if url:
           # Process the provided URL
           pass
   
   # Get the domain from the user
   domain = st.text_input("Enter the domain name (e.g., example.com)")
   
   if st.button("Generate Landing Pages"):
       if domain:
           # Ping Snov.io to get employee emails
           snov_emails = ping_snov(domain)
           
           # Extract attorney names from the website
           attorney_names = extract_attorney_names(f"https://{domain}")
           
           # Match attorney names with emails from Snov.io
           matched_attorneys = match_attorney_emails(attorney_names, snov_emails)
           
           # Find links in the domain
           urls = [f"https://{domain}"]
           # Implement logic to find additional relevant links
           
           # Scrape and convert websites to Markdown
           markdown_files = scrape_and_convert(urls)
           combined_markdown = combine_markdown_files(markdown_files)
           
           # Ask questions and generate landing pages
           questions = [
               # Add your questions here
           ]
           answers = ask_questions_with_openai(combined_markdown, questions)
           
           # Process and save the generated landing pages
           process_and_save_landing_pages(answers, domain)
           
           st.success("Landing pages generated successfully!")
       else:
           st.warning("Please enter a domain name.")

def process_and_save_landing_pages(answers, domain):
   # Implement logic to process the answers and generate landing pages
   # Save the landing pages to a directory based on the domain name
   pass

if __name__ == "__main__":
   main()