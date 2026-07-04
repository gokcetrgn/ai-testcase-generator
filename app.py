from google import genai
from dotenv import load_dotenv
from excel_generator import create_excel
import json
import os

# .env dosyası
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

requirement = input("Requirement: ")

prompt = f"""
You are a Senior QA Engineer.

Generate manual functional test cases.

Return ONLY valid JSON.

Do not write explanations.
Do not use markdown.
Do not wrap the response inside ```json.

Return this exact structure:

[
  {{
    "Test Case ID": "TC001",
    "Title": "",
    "Preconditions": "",
    "Data":"",
    "Steps": [
      "",
      ""
    ],
    "Expected Result": "",
    "Actual Result":"",
    "Priority": "High"
  }}
]

Requirement:
{requirement}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

json_text = response.text

test_cases = json.loads(json_text)

create_excel(test_cases)

print("Excel oluşturuldu.")