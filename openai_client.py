# openai_client.py
import re
import openai
import os
from dotenv import load_dotenv
from config import SYSTEM_PROMPT

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def translate_text(text, source_lang, target_lang):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT.format(source_lang=source_lang,target_lang=target_lang)},
                {"role": "user", "content": text}
            ],
            temperature=0.3
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        raise Exception(f"Translation error: {str(e)}")
    
def check_telugu_text(headline,summary):
    prompt = f"""
    Please check the following Telugu news headline and summary for grammar, meaning, sentence formation and spelling errors. Also check if the news headline matches the summary.
    If there are any mistakes, provide the corrected version. If there are no mistakes, 
    return the original text unchanged.

    Telugu headline: {headline}
    Telugu summary:{summary}
    
    Please return your response in the following format:
    Corrected Telugu headline: [corrected headline]
    Corrected Telugu summary: [corrected summary]
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a Telugu language expert."},
            {"role": "user", "content": prompt}
        ]
    )
    print("checked")
    corrected_text = response.choices[0].message['content'].strip()
    
        
    
    
    # Parse the corrected text to extract headline and summary
    corrected_headline_match = re.search(r"Corrected Telugu headline:\s*(.*?)\s*Corrected Telugu summary:", corrected_text, re.DOTALL)
    corrected_summary_match = re.search(r"Corrected Telugu summary:\s*(.*)", corrected_text, re.DOTALL)
    
    if corrected_headline_match and corrected_summary_match:
        corrected_headline = corrected_headline_match.group(1).strip()
        corrected_summary = corrected_summary_match.group(1).strip()
    else:
        print("Failed to parse corrected text. Using original text.")
        corrected_headline = headline
        corrected_summary = summary
    
    return corrected_headline, corrected_summary



def evaluate_telugu_article(headline,summary, original_article):
    prompt = f"""
    Please evaluate the following Telugu summary and headline generated from Telugu article based on these aspects:

    1. Grammar
    2. Punctuation
    3. Spelling
    4. Logical Consistency
    5. Clarity & Readability
    6. Style & Tone
    7. Faithfulness to Original

    For each aspect, provide a score out of 10 and offer suggestions for improvement.
    Also provide an overall summary of improvements.

    Telugu Summary and Headline to be evaluated:
    Headline:{headline}
    Summary:{summary}

    Original Article for comparison:
    {original_article}

    Please format your response as follows:

    1. Grammar:
    Score: /10
    Issues & Suggestions:

    2. Punctuation:
    Score: /10
    Issues & Suggestions:

    3. Spelling:
    Score: /10
    Issues & Suggestions:

    4. Logical Consistency:
    Score: /10
    Issues & Suggestions:

    5. Clarity & Readability:
    Score: /10
    Issues & Suggestions:

    6. Style & Tone:
    Score: /10
    Issues & Suggestions:

    7. Faithfulness to Original:
    Score: /10
    Issues & Suggestions:

    Summary of Improvements:
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a Telugu language expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        raise Exception(f"Evaluation error: {str(e)}")
