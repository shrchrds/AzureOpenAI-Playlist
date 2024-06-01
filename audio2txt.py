import os
from openai import AzureOpenAI
from dotenv import load_dotenv
import requests

load_dotenv()
AZURE_OPENAI_API_KEY=os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

whisper_model="audio2text"
chat_model="gpt-35-turbo"
region="northcentralus"

final_url = f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{whisper_model}/audio/transcriptions?api-version=2023-09-01-preview"

headers = {
    "api-key": AZURE_OPENAI_API_KEY,
}

file_path = r"Data\audio.mp3"

# Open the file in binary mode and close it after reading
with open(file_path, "rb") as file:
    files = {"file": (os.path.basename(file_path), file, "application/octet-stream")}

    final_response = requests.post(final_url, headers=headers, files=files).json()
    print(final_response)
    
    user_prompt=final_response['text']
    
    client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY
    )

    completion = client.chat.completions.create(
    model=chat_model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_prompt}
    ]
    )
  
    print(completion.choices[0].message.content)
