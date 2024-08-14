# Telugu News Article Summarizer and Title Generator

It summarizes Telugu news articles and generate titles. It uses AWS Bedrock for text analysis.

## Features

- Input Telugu news articles (300-500 words)
- Generate engaging headlines in Telugu
- Create concise summaries in Telugu
- User-friendly Streamlit interface
- FastAPI backend for processing

## Prerequisites

- Python 3.7+
- AWS account with Bedrock access
- OpenAI API key

## Structure

- `main.py`: FastAPI application
- `streamlit_app.py`: Streamlit user interface
- `bedrock_client.py`: AWS Bedrock client
- `openai_client.py`: OpenAI client for translations
- `config.py`: Configuration and static variables
- `.env`: Environment variables
  
## API Endpoints

- `POST /analyze`: Analyzes a Telugu news article
- Request body: `{"text": "Your Telugu article here"}`
- Response: JSON containing Telugu and English versions of the title, summary, and full text translation

## Configuration

- `BEDROCK_MODEL_ID`: The AWS Bedrock model ID
- `BEDROCK_REGION`: AWS region for Bedrock
- `SYSTEM_PROMPT`: The system prompt for translations
- `NEWS_PROMPT`: The prompt template for news article analysis
