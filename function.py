import re
import pandas as pd
from bedrock_client import BedrockClient
from openai_client import translate_text
from config import NEWS_PROMPT,TELUGU_CHECK_PROMPT
import os
from dotenv import load_dotenv
# Add this import

# Load environment variables
load_dotenv()
def analyze_article(article_text: str):
    try:
        bedrock_client = BedrockClient()

        # Translate the entire original article
        english_full_text = translate_text(article_text,"telugu","english")
        
        # Analyze with Bedrock
        prompt = NEWS_PROMPT.format(article=article_text)
        response = bedrock_client.analyze_json(prompt)
        
        # Extract title and summary
        title_match = re.search(r"హెడ్‌లైన్:\s*(.*)\s*సారాంశం:", response)
        summary_match = re.search(r"సారాంశం:\s*(.*)", response)
        
        if title_match and summary_match:
            telugu_title = title_match.group(1).strip()
            telugu_summary = summary_match.group(1).strip()
            
            check_prompt = TELUGU_CHECK_PROMPT.format(headline=telugu_title, summary=telugu_summary)
            check_response = bedrock_client.analyze_json(check_prompt)
            
            # Extract the corrected headline and summary
            corrected_headline_match = re.search(r"Telugu headline:\s*(.*?)\s*Telugu summary:", check_response, re.DOTALL)
            corrected_summary_match = re.search(r"Telugu summary:\s*(.*)", check_response, re.DOTALL)
            
            
            if corrected_headline_match and corrected_summary_match:
                corrected_telugu_title = corrected_headline_match.group(1).strip()
                corrected_telugu_summary = corrected_summary_match.group(1).strip()
            else:
                print("Warning: Failed to parse the corrected text. Using original generated text.")
                corrected_telugu_title = telugu_title
                corrected_telugu_summary = telugu_summary
            
            # Translate title and summary to English
            english_title = translate_text(telugu_title,"telugu","english")
            english_summary = translate_text(telugu_summary,"telugu","english")
            
            
            return {
                "telugu_article": article_text,
                "english_translated_article": english_full_text,
                "telugu_summary": telugu_summary,
                "english_summary": english_summary,
                "telugu_title": telugu_title,
                "english_title": english_title,
                "corrected_telugu_title": corrected_telugu_title,
                "corrected_telugu_summary": corrected_telugu_summary
            }
        else:
            print("Error: Failed to parse the generated response. The response format might be incorrect.")
            return None
    except Exception as e:
        print(f"Error occurred during article analysis: {str(e)}")
        return None

def update_excel(file_name, new_data):
    
    if new_data is None:
        return
    
    if os.path.exists(file_name):
        existing_df = pd.read_excel(file_name)
        updated_df = pd.concat([existing_df, pd.DataFrame([new_data])], ignore_index=True)
    else:
        updated_df = pd.DataFrame([new_data])
    
    updated_df.to_excel(file_name, index=False)

if __name__ == "__main__":
    aws_key = os.getenv('AWS_KEY')
    aws_secret_key = os.getenv('AWS_SECRET_KEY')
    
    if aws_key:
        print(f"AWS Key: {aws_key}")
    else:
        print("AWS Key not found in environment variables")
    
    if aws_secret_key:
        print(f"AWS Secret Key: {aws_secret_key}")
    else:
        print("AWS Secret Key not found in environment variables")

    
    input_file = "input.txt"
    
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            article_text = file.read().strip()
        
        if article_text:
            result = analyze_article(article_text)
            if result is not None:
                # Update the main Excel file
                main_file = "article_analysis.xlsx"
                update_excel(main_file, result)
                
                # Update the Telugu-only Excel file
                telugu_file = "telugu_analysis.xlsx"
                telugu_data = {
                    "telugu_article": result["telugu_article"],
                    "article_summary": result["telugu_summary"],
                    "article_title": result["telugu_title"]
                }
                update_excel(telugu_file, telugu_data)
                
                print("Results updated in Excel files.")
            else:
                print("Failed to analyze the article. No updates made to Excel files.")
        else:
            print("The input file is empty.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the input file: {str(e)}")


print("Check the Excel files for results.")
