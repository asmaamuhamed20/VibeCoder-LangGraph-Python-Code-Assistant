import os
from dotenv import load_dotenv
import requests

# Load .env file
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("BASE_URL", "https://openrouter.ai/api/v1")


def call_llm(task, user_input, examples):
    examples_text = "\n".join([ex["code"] for ex in examples])
    prompt = f"Task: {task}\nUser Input:\n{user_input}\nExamples:\n{examples_text}\nResponse:"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "http://localhost:5000", 
        "X-Title": "LangGraph_Code_Assistant"
    }

    response = requests.post(
        f"{BASE_URL}/chat/completions",
        headers=headers,
        json={
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
    )
    
    return response.json()["choices"][0]["message"]["content"]



