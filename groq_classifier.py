from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def classify_task(text: str) -> bool:
    """Return True if text contains a task."""
    prompt = f"""
    You are a classifier. Determine if the email contains a task.
    Respond only YES or NO.

    Email content:
    {text}
    """

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=5,
        temperature=0
    )

    answer = response.choices[0].message.content.strip().upper()
    return answer == "YES"

