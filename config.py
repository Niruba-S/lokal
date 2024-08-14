
BEDROCK_MODEL_ID = "anthropic.claude-3-5-sonnet-20240620-v1:0"
BEDROCK_REGION = "us-east-1"

SYSTEM_PROMPT = """You are a professional translator specializing in {target_lang} and Telugu. Translate the following text accurately to {target_lang}, preserving all proper names, team names, and specific details."""

NEWS_PROMPT = """As an experienced Telugu newspaper editor, create an engaging short headline and concise summary only from the following Telugu news article. Strictly follow the guidelines below and don't generate anything out of context:

Headline:
-Craft a compelling headline that captures the core of the article in a captivating way that compels readers to read more, only from the article content(5-9words)
-Use active, vivid language that sparks curiosity and interest.
-Use dynamic, strong verbs to make it impactful.
-Incorporate key elements from the article to ensure it's relevant and eye-catching.       
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
{article}

Respond in this format:
హెడ్‌లైన్: [Your engaging short Telugu headline]
సారాంశం: [Your concise Telugu summary with all critical information]

Important: Ensure that all information in the headline and summary is directly derived from the given article. Do not introduce any information that is not present in the original text. Retain and accurately represent all numbers, statistics, and vital details from the original article in the summary."""