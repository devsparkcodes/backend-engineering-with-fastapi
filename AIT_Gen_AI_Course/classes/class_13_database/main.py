from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def func(ask: dict):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
                {"role": "user", "content": ask}
        ]
    )
    
    return response.choices[0].message.content
