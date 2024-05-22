from for_testing_streamlit_sfl import extract_attorneys_from_domain, app  # Import your Flask app

def test_extract_attorneys():
    test_domain = "wylylawfirm.com"  # Replace with a domain you want to test
    try:
        print(f"Testing extract_attorneys_from_domain with domain: {test_domain}")
        
        with app.app_context():  # Set up the application context
            response = extract_attorneys_from_domain(test_domain)
            response_data = response.get_json()
            print(f"Response JSON: {response_data}")
            
            navigation_links = response_data.get('all_nav_links', [])
            attorney_names = response_data.get('attorney_names', [])
            
            print(f"Navigation Links: {navigation_links}")
            print(f"Attorney Names: {attorney_names}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_extract_attorneys()