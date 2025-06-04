

import openai
import json
import os
from dotenv import load_dotenv
from transformers import pipeline

#
# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")
#
# def generate_specifications(text_description):
#     prompt = f"""
#         You receive the content of a complete construction document and you need to extract and summarize all structural parameters - such as material types, thicknesses, usage classifications, and compliance standards - from that document into clean JSON.
#         Reply in JSON format only No further comments!
#         The content of the document is:
#         {text_description}
#     """
#
#     response = openai.chat.completions.create(
#         model="gpt-4",
#         messages=[
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0
#     )
#     content = response.choices[0].message.content.strip()
#     try:
#         result_json = json.loads(content)
#     except json.JSONDecodeError:
#         return None
#
#     return result_json
#
# if __name__ == "__main__":
#     f = open("construction specification.txt", 'r', encoding='utf-8')
#     description = f.readlines()
#     result = generate_specifications(description)
#     if result:
#         with open("results/specifications.json", "w") as f:
#             json.dump(result, f, indent=2)
#         print("✅ specifications.json created")


with open(r"C:\Users\1\Downloads\for_test.txt", "r", encoding="utf-8") as f:
    spec_text = f.read()

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

input_text = f"""
Please extract and convert the following construction specification into structured JSON.
Each entry should include:
component name
materials
dimensions 
classification 
any standards mentioned

TEXT:
{spec_text}

Return ONLY JSON without any extra text.
"""

result = generator(input_text, max_length=512, do_sample=False)
generated_text = result[0]['generated_text']

try:
    data = json.loads(generated_text)
    print("Parsed JSON:", data)
except json.JSONDecodeError:
    print("Failed to parse JSON. Here is the raw output:")
    print(generated_text)
    data = None

output_dir = "RESULTS"
os.makedirs(output_dir, exist_ok=True)

if data is not None:
    output_path = os.path.join(output_dir, "specifications.json")
    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f"JSON saved successfully to {output_path}")
else:
    print("No valid JSON to save.")
