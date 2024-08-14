import boto3
import json
import os
from dotenv import load_dotenv
from config import BEDROCK_MODEL_ID, BEDROCK_REGION

load_dotenv()

class BedrockClient:
    def __init__(self):
        self.aws_key = os.getenv('AWS_ACCESS_KEY_ID')
        self.aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        self.client = boto3.client(
            service_name='bedrock-runtime',
            region_name=os.getenv('AWS_REGION'),
            aws_access_key_id=self.aws_key,
            aws_secret_access_key=self.aws_secret_key
        )

    def analyze_json(self, prompt):
        try:
            body = json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 1000,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.3,
                "top_p": 0.9
            })
            
            response = self.client.invoke_model(body=body, modelId=BEDROCK_MODEL_ID, accept="application/json", contentType="application/json")
            response_body = json.loads(response.get('body').read())
            result = response_body['content'][0]['text']
            return result
        except Exception as e:
            raise Exception(f"Bedrock error: {str(e)}")
