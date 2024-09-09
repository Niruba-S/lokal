from config import TELUGU_CHECK_PROMPT
from bedrock_client import BedrockClient

bedrock_client = BedrockClient()

telugu_title="కేన్స్‌లో భార లఘు చిత్రానికి అగ్రస్థనం"
telugu_summary="కేన్స్‌-2024లో 'సన్‌ఫ్లవర్స్‌ వర్‌ ద ఫస్ నో' అనే భారతీయ ల చిత్రం ఉత్తమ లఘు చిత్రంగా ఎం. చిదాద దర్శకత్వంలో తెరకెక్కిన ఈ 16 నిమిషాల చిత్రం 17 దేశాల చిత్రాలను అధిగమించింది. మహేశ్వరి రూపొందించిన 'బన్నీ హుడ్‌' తృతీయ స్థానం సాధించింది. ఉత్తమ లఘు చిత్రానికి 15,000 యూరోలు, తృతీయ స్థానికి 7,500 యూరోలు బహుమతిగా లభించాయి"

check_prompt = TELUGU_CHECK_PROMPT.format(headline=telugu_title, summary=telugu_summary)
check_response = bedrock_client.analyze_json(check_prompt)
print(check_response)
