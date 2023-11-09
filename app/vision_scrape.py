
from openai import OpenAI
import base64
from dotenv import load_dotenv
import os
import json

load_dotenv()

# openai_api_key=os.getenv("OPENAI_API_KEY")

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

image_path = "./gio-law.com_.png"
base64_image = encode_image(image_path)

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """
                    This image is a Figma mockup of a ficticious law firm. To make sure I am not making any spelling mistakes, return 
                    1. Header Section:
                        - Logo
                        - Navigation Bar

                    2. Main Banner Section:
                    - Main Title
                    - Tagline
                    - Call-to-Action Button

                    3. Introductory Section:
                    - Heading
                    - Description Text
                    - Call-to-Action Button

                    4. Services Overview Section:
                    - Subsections with Images and Service Titles

                    5. Specialization Section:
                    - List of Specializations

                    6. Additional Services Section:
                    - Service Titles with Call-to-Action Buttons

                    7. Testimonials Section:
                    - Testimonial Quotes
                    - Rating Indicators
                    - Attribution

                    8. Profiles Section:
                    - Profile Images and Names

                    9. Call-to-Action Section:
                    - Promotional Tagline
                    - Contact Information
                    - Secondary Call-to-Action Button

                    10. Footer Section:
                    - Multiple Columns with Information Categories
                    
                    no need for any full sentences.
                    """
                    # "text": "This image is a Figma mockup of a ficticious law firm. Breakdown the layout of this page. Make sure not to leave anything out. You can group the subsections into larger sections. Just list the names of the subsections and sections. no need for the content inside of it."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"
                    }
                }
            ],
        }
    ],
    max_tokens=500,
)

response_dict = json.loads(response.json())
print(response_dict['choices'][0]['message']['content'])

