import json
import requests

def extract_urls_and_links_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    completed_urls_and_links = []

    for item in data:
        if item["Done"] == "No":
            links = json.loads(item["links"])
            # Call the build_the_site endpoint with the links
            response = requests.post('http://127.0.0.1:5000//build_the_site', json={'urls': links})
            if response.status_code == 200:
                item["Done"] = "Yes"
                completed_urls_and_links.append(item)
            else:
                print(f"Failed to build the site for {item['URL']}. Status Code: {response.status_code}, Error: {response.text}")

    # Write the updated data back to the original JSON file
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

    # Write completed URLs and links to a new JSON file
    with open('csv_for_build_the_site_done.json', 'w', encoding='utf-8') as done_file:
        json.dump(completed_urls_and_links, done_file, indent=4)

# Example usage
file_path = 'csv_for_build_the_site.json'
extract_urls_and_links_from_json(file_path)