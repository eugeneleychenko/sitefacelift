import csv
import json
from for_testing_streamlit_sfl import extract_attorneys_from_domain
from flask import Flask
import signal

app = Flask(__name__)

def timeout_handler(signum, frame):
    raise TimeoutError("Function execution timed out.")


def process_domains_and_generate_csv(input_csv, output_csv):
    print("Opening input CSV file...")
    with open(input_csv, 'r') as infile:
        domains = [line.strip() for line in infile]
        print(f"Read {len(domains)} domains from the input CSV.")
        print(f"Domains: {domains}")

    print("Opening output CSV file...")
    with open(output_csv, 'a', newline='') as outfile:
        print("Output CSV file opened successfully.")
        writer = csv.writer(outfile, delimiter='$')
        writer.writerow(['Domain', 'Navigation Links'])  # Remove 'Attorney Names' header
        print("Output CSV file initialized with headers.")

        for domain in domains:
            print(f"Processing domain: {domain}")
            try:
                with app.app_context():
                    # Set a timeout of 10 seconds
                    signal.signal(signal.SIGALRM, timeout_handler)
                    signal.alarm(10)

                    try:
                        # Extract navigation links
                        print(f"Calling extract_attorneys_from_domain for {domain}")
                        response = extract_attorneys_from_domain(domain)
                        print(f"Received response for {domain}: {response}")
                        
                        if isinstance(response, tuple):
                            response_data = response[0].get_json()
                        else:
                            response_data = response.get_json()
                        
                        print(f"Parsed JSON response for {domain}: {response_data}")
                        
                        navigation_links = response_data.get('all_nav_links', [])
                        print(f"Extracted navigation links for {domain}: {navigation_links}")

                        # Convert list to comma-separated string
                        navigation_links_str = ','.join(navigation_links)

                        # Write to CSV immediately
                        writer.writerow([domain, navigation_links_str])
                        print(f"Successfully wrote data for {domain} to CSV.")
                    except TimeoutError:
                        print(f"Timeout occurred while processing {domain}. Moving to the next URL.")
                        writer.writerow([domain, 'Timeout'])
                    except Exception as e:
                        print(f"An error occurred while processing {domain}: {e}")
                        writer.writerow([domain, 'Error'])
                    finally:
                        # Cancel the alarm
                        signal.alarm(0)
            except Exception as e:
                print(f"An error occurred while processing {domain}: {e}")
                writer.writerow([domain, 'Error'])

            # Remove the processed domain from the input file
            domains.remove(domain)
            with open(input_csv, 'w') as infile:
                infile.writelines(domain + '\n' for domain in domains)

# Define the input and output CSV file paths
input_csv = 'nav_attorney_source.csv'
output_csv = 'attorney_names_output.csv'

# Process the domains from the input CSV and generate the output CSV
print("Starting the CSV processing...")
process_domains_and_generate_csv(input_csv, output_csv)
print("CSV processing completed.")