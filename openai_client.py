# openai_client.py

import openai
import os
from dotenv import load_dotenv
from config import SYSTEM_PROMPT

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def translate_text(text, target_lang='en'):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT.format(target_lang=target_lang)},
                {"role": "user", "content": text}
            ],
            temperature=0.3
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        raise Exception(f"Translation error: {str(e)}")