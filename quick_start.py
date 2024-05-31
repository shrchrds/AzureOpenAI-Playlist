import os
from openai import AzureOpenAI
import json
from dotenv import load_dotenv

load_dotenv()
AZURE_OPENAI_API_KEY=os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint= AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY
)

completion = client.chat.completions.create(
    model="gpt-35-turbo",
    messages=[
        {
            "role": "user",
            "content": "Who is the founder of Mistral?",
        }
    ]
)
      
response_dict = json.loads(completion.to_json())
print(response_dict['choices'][0]['message']['content'])