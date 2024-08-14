from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bedrock_client import BedrockClient
from openai_client import translate_text
from config import NEWS_PROMPT
import re
import uvicorn
app = FastAPI()
bedrock_client = BedrockClient()

class Article(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_article(article: Article):
    try:
        # Translate the entire original article
        english_full_text = translate_text(article.text)
        
        # Analyze with Bedrock
        prompt = NEWS_PROMPT.format(article=article.text)
        response = bedrock_client.analyze_json(prompt)
        
        # Extract title and summary
        title_match = re.search(r"హెడ్‌లైన్:\s*(.*)\s*సారాంశం:", response)
        summary_match = re.search(r"సారాంశం:\s*(.*)", response)
        
        if title_match and summary_match:
            telugu_title = title_match.group(1).strip()
            telugu_summary = summary_match.group(1).strip()
            
            # Translate title and summary to English
            english_title = translate_text(telugu_title)
            english_summary = translate_text(telugu_summary)
            
            return {
                "telugu_title": telugu_title,
                "telugu_summary": telugu_summary,
                "english_title": english_title,
                "english_summary": english_summary,
                "english_full_text": english_full_text
            }
        else:
            raise HTTPException(status_code=500, detail="Failed to parse the generated response")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)