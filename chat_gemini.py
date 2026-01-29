from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyDAI6Z1QMN9hCGc1YuZqEhh8keNXV0tzmQ')

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents={'text': 'Why is the sky blue?'},
    config={
        'temperature': 0,
        'top_p': 0.95,
        'top_k': 20,
    },
)

print(response.text)
