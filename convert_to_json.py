import json
import os
from transformers import pipeline

with open(r"C:\Users\1\Downloads\for_test.txt", "r", encoding="utf-8") as f:
    spec_text = f.read()

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

input_text = f"""
Please extract and convert the following construction specification into structured JSON.
Each entry should include:
component name
materials
dimensions (if available)
classification (e.g. wall, floor, ceiling)
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
