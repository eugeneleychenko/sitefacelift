import requests

def fetch_serp_api_results(api_key, query, start_page, end_page):
    for page in range(start_page, end_page + 1):
        params = {
            "q": query,
            "location": "New York,NY",
            "hl": "en",
            "gl": "us",
            "google_domain": "google.com",
            "api_key": api_key,
            "start": (page - 1) * 10
        }
        response = requests.get("https://serpapi.com/search", params=params)
        results = response.json().get("organic_results", [])
        
        for result in results:
            position = result.get("position")
            title = result.get("title")
            url = result.get("link")
            print(f"{position}. {title} - {url}")

api_key = "b2d29d50643af9d353256811e054b024e14643d71cd3dcabcfc068c1023962aa"
query = "new york law firm"
start_page = 21
end_page = 25

fetch_serp_api_results(api_key, query, start_page, end_page)
