import streamlit as st
import boto3
import json
import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def analyze_json(prompt):
    try:
        AWS_KEY = os.getenv('AWS_KEY')
        AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
        bedrock_runtime = boto3.client(
            service_name='bedrock-runtime',
            region_name='us-east-1',
            aws_access_key_id=AWS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )
        
        modelId = "anthropic.claude-3-5-sonnet-20240620-v1:0"
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.3,  # Reduced temperature for more focused outputs
            "top_p": 0.9  # Slightly reduced top_p for more conservative text generation
        })
        
        response = bedrock_runtime.invoke_model(body=body, modelId=modelId, accept="application/json", contentType="application/json")
        response_body = json.loads(response.get('body').read())
        result = response_body['content'][0]['text']
        return result
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

def translate_text(text, target_lang='en'):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a professional translator specializing in {target_lang} and Telugu. Translate the following text accurately to {target_lang}, preserving all proper names, team names, and specific details."},
                {"role": "user", "content": text}
            ],
            temperature=0.3  # Lower temperature for more accurate translations
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        st.error(f"Translation error: {str(e)}")
        return None

st.set_page_config(layout="wide")

st.title("Telugu News Article Summarizer and Title Generator")

telugu_text = st.text_area("Enter Telugu News Article (300-500 words):", height=200)

if st.button("Summarize and Generate Title"):
    if telugu_text:
        with st.spinner("Processing..."):
            # Translate the entire original article
            english_full_text = translate_text(telugu_text)
            
            prompt = f"""As an experienced Telugu newspaper editor, create an engaging short headline and concise summary only from the following Telugu news article. Strictly follow the guidelines below and don't generate anything out of context:

                        Headline:
                        -Craft a compelling headline that captures the core of the article in a captivating way that compels readers to read more, only from the article content(5-9words)
                        -Use active, vivid language that sparks curiosity and interest.
                        -Use dynamic, strong verbs to make it impactful.
                        -Incorporate key elements from the article to ensure it’s relevant and eye-catching.       
                        -Aim for a tone that matches the article's content
                        -Use appropriate punctuations if needed.(?,! etc.,)
                        -Ensure all names and proper nouns are spelled correctly


                        Summary:

                        -Write a concise summary in Telugu (150-200 words)
                        -Capture the essence of the article
                        -Include all key facts: who, what, when, where, why, and how
                        -Most important-accuracy
                        -Retain all numbers, statistics, and critical information accurately
                        -Use journalistic style: clear, concise, and objective
                        -Mention all specific names involved in the incident
                        -Ensure no vital information is lost in summarization
                        -Double-check all facts and figures for accuracy



                        Article:
                        {telugu_text}
                        Respond in this format:
                        హెడ్‌లైన్: [Your engaging short Telugu headline]
                        సారాంశం: [Your concise Telugu summary with all critical information]
                        Important: Ensure that all information in the headline and summary is directly derived from the given article. Do not introduce any information that is not present in the original text. Retain and accurately represent all numbers, statistics, and vital details from the original article in the summary.
                        """
            
            response = analyze_json(prompt)
            
            if response:
                # Extract title and summary using regex to avoid duplicate labels
                import re
                
                title_match = re.search(r"హెడ్‌లైన్:\s*(.*)\s*సారాంశం:", response)
                summary_match = re.search(r"సారాంశం:\s*(.*)", response)
                
                if title_match and summary_match:
                    telugu_title = title_match.group(1).strip()
                    telugu_summary = summary_match.group(1).strip()
                    
                    # Translate title and summary to English
                    english_title = translate_text(telugu_title)
                    english_summary = translate_text(telugu_summary)
                    
                    # Display results with improved layout
                    st.success("Processing complete!")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("Original Article (Telugu)")
                        st.markdown(f"<div style='background-color: #f0f2f6; padding: 10px; font-size: 16px;'>{telugu_text}</div>", unsafe_allow_html=True)
                        
                        st.subheader("Generated Content (Telugu)")
                        st.markdown(f"**హెడ్‌లైన్:** {telugu_title}")
                        st.markdown(f"**సారాంశం:** {telugu_summary}")
                    
                    with col2:
                        st.subheader("Full English Translation")
                        st.markdown(f"<div style='background-color: #f0f2f6; padding: 10px; font-size: 16px;'>{english_full_text}</div>", unsafe_allow_html=True)
                        
                        st.subheader("English Translations")
                        st.markdown(f"**Headline:** {english_title}")
                        st.markdown(f"**Summary:** {english_summary}")
                else:
                    st.error("Failed to parse the generated response. Please try again.")
            else:
                st.error("Failed to generate summary and title. Please try again.")
    else:
        st.warning("Please enter a Telugu news article.")