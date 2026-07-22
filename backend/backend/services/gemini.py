import os

def generate_gemini_reply(message):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Gemini API key not configured."

    # Real Gemini API integration next step me add karenge
    return f"Gemini AI received: {message}"
