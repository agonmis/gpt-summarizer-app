from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def callOpenAI(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Du bist ein exzellenter Zusammenfasser. Bitte den vorgegebenen Text in maximal zwei Sätzen zusammenfassen"
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content
