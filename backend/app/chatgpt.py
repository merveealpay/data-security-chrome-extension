import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key here
openai.api_key = os.getenv("OPENAI_API_KEY")

async def check_sensitive_data(data: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful data security assistant."},
            {"role": "user", "content": f"Check if the following data contains any sensitive information:\n{data}"}
        ]
    )
    return response['choices'][0]['message']['content'].strip()
