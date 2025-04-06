from app.config import settings
from groq import Groq

def get_ai_response(ai_request):
    client = Groq(api_key=settings.groq_api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": ai_request.message,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content
