from dotenv import load_dotenv
import os

load_dotenv()

together_api_key = os.getenv('TOGETHER_API_KEY')
url = "https://api.together.xyz/inference"

headers = {
    "Authorization": f"Bearer {together_api_key}",
    "Content-Type": "application/json"
}

model = "togethercomputer/llama-2-7b-chat"

temperature = 0.7
max_tokens = 500