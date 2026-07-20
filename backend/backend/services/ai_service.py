import os

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

def generate_reply(message):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key or OpenAI is None:
        return "OpenAI API key not configured."

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are Jarvis AI, a helpful personal assistant."},
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content
