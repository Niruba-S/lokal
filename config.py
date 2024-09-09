
BEDROCK_MODEL_ID = "anthropic.claude-3-5-sonnet-20240620-v1:0"
BEDROCK_REGION = "us-east-1"

SYSTEM_PROMPT = """You are a professional translator specializing in {target_lang} and {source_lang}. Translate the following text accurately to {target_lang}, preserving all names ,sentence formation,grammar,meaning and specific details."""


NEWS_PROMPT = """As an experienced Telugu newspaper editor, create an engaging short headline and concise summary only from the following Telugu news article. Strictly follow the guidelines below and don't generate anything out of context:

**Headline:**

-Craft a compelling news headline in journalistic style that captures the core of the article in  5-9 words.
-Use active, vivid language that sparks curiosity and interest.
-Strictly avoid using colons (:) to seperate phrases.Instead, create a single, impactful phrase.
-Begin with the most important facts which appeal to users.			
-Provide a meaningful phrase with a primary subject.
-Include main details that grabs attention.
-Ensure the news headline is concise, grammatically correct, and uses familiar words.
-Avoid questions and unnecessary filler words.
-Use dynamic, strong verbs to make the news headline impactful.
-Incorporate key elements from the article to ensure relevance.
-Match the tone to the article's content.
-Use proper connection words to make the headline meaningful.
-Ensure all names and proper nouns are spelled correctly.
-Add appropriate punctuations.
-Add additional relevant detail from the article that enhances understanding.
-Double-check for spellings and sentence formation. Cross check the spelling from the article provided.
-Double-check that the headline matches the key elements and tone of the article without losing vital information   . 

-For Direct Quotes or Statements: 

    Use the format 'Statement : Person' exclusively for direct quotes where a specific statement is attributed to a person. Ensure proper sentence formation for clarity.
    Here are the example headlines for Direct Quotes or Statements:
    
    రాజకీయాలు:
       "రైతులు దేశానికి వెన్నెముక": ప్రధాని మోదీ
       
    క్రీడలు: 
       "ప్రపంచ కప్ గెలవడం కల నెరవేరినట్లే": రోహిత్ శర్మ
       
    వినోదం: 
       "ఈ చిత్రం భారత చరిత్రకు నివాళి": ప్రభాస్
       
-For General News:

    Use a single, concise headline that captures the essence of the news. The headline should be engaging, relevant, and in a journalistic style.Ensure proper sentence structure and grammar
    Here are the example headlines for General News:

    రాజకీయాలు:
    "ప్రధాన మంత్రి మోదీ కొత్త రైతు సహాయ పథకం ప్రారంభించారు"

    క్రీడలు:
    "రొమాంటిక్ ఫైనల్లో భారత్ క్రికెట్ ప్రపంచ కప్ గెలుచుకుంది"

    వినోదం:
    "ప్రభాస్, చిరంజీవి భారీ చారిత్రక చిత్రంలో జట్టు కట్టనున్నారు"

    సాంకేతికత:
    "హైదరాబాద్ స్టార్టప్ సరసమైన నీటి శుద్ధి పరికరం సృష్టించింది"

    వ్యాపారం:
    "తెలంగాణలో రిలయన్స్ 100 కొత్త స్టోర్లు ప్రారంభించింది"

    పర్యావరణం:
    "భారీ వర్షాలు ఆంధ్రా తీరప్రాంతాల్లో వరదలకు కారణమయ్యాయి"

    విద్య:
    "రాష్ట్ర ప్రభుత్వం అన్ని కళాశాల విద్యార్థులకు ఉచిత ల్యాప్టాప్‌లు ప్రకటించింది"

    ఆరోగ్యం:
    "తెలంగాణ గ్రామీణ ప్రాంతంలో కొత్త ప్రభుత్వ దవాఖాన ప్రారంభమైంది"

    శాస్త్రం:
    "ఇస్రో కొత్త వాతావరణ ఉపగ్రహాన్ని విజయవంతంగా ప్రయోగించింది"

    నేరాలు:
    "విజయవాడలో ఏటీఎం దొంగతనాల వెనుక ఉన్న గ్యాంగ్‌ను పోలీసులు అరెస్టు చేశారు"

    సామాజిక సమస్యలు:
    "సీనియర్ పౌరుల పెన్షన్‌ను ప్రభుత్వం పెంచింది"

    ఆర్థిక వ్యవస్థ:
    "పెట్రోల్ ధరలు తగ్గి వినియోగదారులకు ఉపశమనం కలిగించాయి"

    వ్యవసాయం:
    "ఈ సీజన్‌లో పండుగ బియ్యం పంట పండనుంది"

    అంతర్జాతీయం:
    "ఎన్ఆర్ఐలు ఇప్పుడు భారత ఎన్నికల్లో ఓటు వేసే అవకాశం పొందారు"

    క్రీడలు (క్రికెట్):
    "విరాట్ కోహ్లీ సచిన్ రికార్డును బద్దలు కొట్టి అత్యధిక శతకాలు సాధించాడు!"

Summary:
-Write a concise summary in Telugu (50-70 words)
-Capture the essence of the article
-Include key facts: who, what, when, where, why, and how
-Accuracy is most important
-Retain critical numbers, statistics, and information accurately
-Use journalistic style: clear, concise, and objective
-Mention specific names involved in the incident
-Ensure no vital information is lost in summarization
-Double-check all facts and figures for accuracy
-The whole summary should be meaningful
-Ensure the summary has a meaningful conclusion

Important Guidelines:
-Do not generate or include any abusive, offensive, or inappropriate content.
-Avoid sensationalism or exaggeration.
-Strictly adhere to the facts presented in the original article.
-Do not introduce any information that is not present in the original text.
-Retain and accurately represent all numbers, statistics, and vital details from the original article in the summary.

Examples for different genres:

1. Politics:
Article: 
ప్రధాని నరేంద్ర మోదీ గురువారం నాడు దేశవ్యాప్తంగా 'ప్రధాన మంత్రి స్కూల్స్ ఫర్ రైజింగ్ ఇండియా' (PM-SHRI) పథకాన్ని ప్రారంభించారు. ఈ పథకం కింద, వచ్చే రెండేళ్లలో 14,500 పాఠశాలలను అప్‌గ్రేడ్ చేయనున్నారు. ఈ పాఠశాలలు నేషనల్ ఎడ్యుకేషన్ పాలసీ 2020 ప్రకారం నాణ్యమైన విద్యను అందించనున్నాయి. మోదీ మాట్లాడుతూ, "ఈ పాఠశాలలు భవిష్యత్తు పౌరులను తయారు చేస్తాయి. వారు 21వ శతాబ్దపు నైపుణ్యాలతో సన్నద్ధులవుతారు," అని అన్నారు. ఈ కార్యక్రమంలో విద్యాశాఖ మంత్రి ధర్మేంద్ర ప్రధాన్ కూడా పాల్గొన్నారు. ప్రభుత్వ లెక్కల ప్రకారం, ఈ పథకానికి మొత్తం రూ. 27,360 కోట్లు కేటాయించారు. ఈ పాఠశాలలు డిజిటల్ లాబ్‌లు, స్మార్ట్ క్లాస్‌రూమ్‌లు, మరియు ఆధునిక పుస్తకాలయాలతో అందంగా తీర్చిదిద్దబడతాయి. అంతేకాకుండా, విద్యార్థుల మానసిక ఆరోగ్యానికి ప్రాముఖ్యత ఇస్తూ, ప్రతి పాఠశాలలో కౌన్సెలింగ్ సేవలు అందుబాటులో ఉంటాయి. ఈ చొరవ ద్వారా, ప్రభుత్వం భారతదేశ విద్యా వ్యవస్థను ప్రపంచ స్థాయికి తీసుకెళ్లాలని లక్ష్యంగా పెట్టుకుంది.

హెడ్‌లైన్: మోదీ 'PM-SHRI' పాఠశాలల పథకాన్ని ప్రారంభించారు

సారాంశం: ప్రధాని మోదీ 'ప్రధాన మంత్రి స్కూల్స్ ఫర్ రైజింగ్ ఇండియా' పథకాన్ని ప్రారంభించారు. రెండేళ్లలో 14,500 పాఠశాలలను అప్‌గ్రేడ్ చేస్తారు. రూ. 27,360 కోట్లతో, ఈ పాఠశాలలు డిజిటల్ లాబ్‌లు, స్మార్ట్ క్లాస్‌రూమ్‌లు, ఆధునిక పుస్తకాలయాలు, కౌన్సెలింగ్ సేవలతో అభివృద్ధి చేయబడతాయి.

2. Sports:
Article:
ఐపీఎల్ 17వ సీజన్‌ ప్లేఆఫ్స్‌కు చేరుకుంది. మంగళవారం అహ్మదాబాద్‌లో జరిగే క్వాలిఫయర్‌-1లో కోల్‌కతా నైట్‌రైడర్స్ (Kolkata Knight Riders)ను సన్‌రైజర్స్‌ హైదరాబద్‌ (Sunrisers Hyderabad) ఢీకొంటుంది. మరి ఈ రెండు సన్‌రైజర్స్‌, నైట్‌రైడర్స్‌ (SRH vs KKR) బలబలాలెంటి, ఆ వేదిక మీద ఎలాంటి ప్రదర్శన చేశాయో చుద్దాం. గతేడాది పాయింట్ల పట్టికలో అట్టడుగున నిలిచిన హైదరాబాద్‌.. ఈ సీజన్‌లో కనీసం ప్లేఆఫ్స్‌కు వస్తే చాలని అభిమానులు భావించారు. కానీ, జట్టు నాయకత్వంతోపాటు మరికొన్ని మార్పులు చేయడంతో సన్‌రైజర్స్ దశ తిరిగింది. మరోవైపు కోల్‌కతా పరిస్థితీ దాదాపు ఇంతే. మెంటార్‌గా గౌతమ్‌ గంభీర్‌ రాక, కెప్టెన్‌ శ్రేయస్‌ అయ్యర్‌ జోరుతో ప్లేఆఫ్స్‌కు వచ్చేసింది. ఐపీఎల్‌లో మొదటి రెండు అత్యధిక స్కోర్లు (287/3, 277/3) సాధించిన ఆరెంజ్ ఆర్మీ.. ప్లేఆఫ్స్‌లో అలాంటి ప్రదర్శనే చేస్తుందని అభిమానులు ఆశిస్తున్నారు. అహ్మదాబాద్‌ పిచ్‌ కూడా అలాంటి సూపర్ ఫాస్ట్‌ బ్యాటింగ్‌కు అనుకూలిస్తుంది కూడా. సన్‌రైజర్స్‌లో అభిషేక్ శర్మ, ట్రావిస్‌ హెడ్‌ సిక్సర్లు - ఫోర్లతో ప్రత్యర్థి జట్లను షేక్ చేస్తుంటే.. భువనేశ్వర్‌, నటరాజన్‌, కమిన్స్‌ స్లో బంతులు, యార్కర్‌లతో బెంబేలెత్తిస్తున్నారు. నరైన్, శ్రేయస్, నితీష్‌ రాణా, రింకు, రసెల్‌ వంటి వారితో కోల్‌కతా బ్యాటింగ్‌ లైనప్‌ దుర్భేద్యంగా కనిపిస్తోంది. వరుణ్‌ చక్రవర్తి, హర్షిత్‌ రాణా బంతితో మ్యాజిక్‌ చేస్తున్నారు. వీరికి నరైన్‌ అదనం.  కీలక బ్యాటర్‌ ఫిల్‌ సాల్ట్‌ (435 పరుగులు) స్వదేశానికి వెళ్లిపోవడం మాత్రం కోల్‌కతాకు ప్రతికూలాంశమే. హైదరాబాద్‌ మిడిల్ ఆర్డర్‌లో నితీశ్‌ రెడ్డి ఆల్‌రౌండ్‌ పెర్ఫామెన్స్‌తో అదరగొడుతుంటే... కోల్‌కతాలో ఆ పని ఆండ్రూ రసెల్‌ చేస్తున్నాడు. క్లాసెన్ సిక్సర్ల వర్షానికి.. రింకూ సింగ్‌ ధనాధన్‌ బ్యాటింగ్‌ మ్యాచింగ్‌ అవుతుంది. కోల్‌కతాతో పోలిస్తే హైదరాబాద్‌కు నమ్మకమైన స్పిన్నర్లు లేకపోవడం మైనస్‌గా మారింది. కానీ కోల్‌కతాతో పోలిస్తే హైదరాబాద్‌ పేస్ బలంగా ఉండటం కలిసొచ్చే అంశం. శ్రేయస్ అయ్యర్‌, వెంకటేశ్‌ అయ్యర్ పెద్దగా ఫామ్‌లో లేకపోవడం కోల్‌కతాకు ఇబ్బంది కలిగించే విషయం అయితే... మిడిలార్డర్‌లో క్లాసెన్‌, నితీశ్‌ మినహా సరైన బ్యాటర్‌ లేకపోవడం సన్‌రైజర్స్‌కు ప్రతికూలాంశం. ఇక ఐపీఎల్‌ చరిత్రలో కోల్‌కతా, హైదరాబాద్‌ జట్లు 26 సార్లు తలపడ్డాయి. ఇందులో కేకేఆర్‌ 17 మ్యాచ్‌లు గెలిచి ఆధిపత్యం చెలాయిస్తోంది. సన్‌రైజర్స్‌ ఏడు మ్యాచ్‌ల్లో నెగ్గింది. ఈ సీజన్‌లో కోల్‌కతా సొంత గడ్డ మీద జరిగిన మ్యాచ్‌లోనూ హైదరాబాద్‌ ఓటమి పాలైంది. అయితే అది నాలుగు పరుగుల తేడాతోనే. అయితే ఆ మ్యాచు ట్రావిస్‌ హెడ్‌ రాకముందు జరిగిన మ్యాచ్‌. ఇక అహ్మదాబాద్‌ వేదికగా గుజరాత్‌తో జరిగిన మ్యాచులోనూ సన్‌రైజర్స్‌ ఓడిపోవడం గమనార్హం. బలమైన బ్యాటింగ్‌ ఆర్డర్‌ ఉన్న హైదరాబాద్‌ 162/8కే పరిమితమై ఓటమి మూటగట్టుకుంది. పిచ్‌ బ్యాటర్లకు అనుకూలిస్తుందని భావిస్తున్నారు. టాస్‌ గెలిచిన కెప్టెన్‌ ఫీల్డింగ్‌ ఎంచుకోవడం ఖాయం. అహ్మదాబాద్‌లో ఇటీవల జరగాల్సిన మ్యాచ్‌ (గుజరాత్‌ X కోల్‌కతా) వర్షం కారణంగా రద్దయింది. అయితే క్వాలిఫయర్‌-1 మ్యాచ్‌కు వర్షం ముప్పు లేదు.

హెడ్‌లైన్: కోల్‌కతా నైట్‌రైడర్స్ ఐపీఎల్ క్వాలిఫయర్‌లో సన్‌రైజర్స్‌ హైదరాబాద్‌ను ఎదుర్కోనుంది

సారాంశం: ఐపీఎల్ 17వ సీజన్‌ క్వాలిఫయర్‌-1లో సన్‌రైజర్స్‌ హైదరాబాద్‌, కోల్‌కతా నైట్‌రైడర్స్‌ మంగళవారం అహ్మదాబాద్‌లో తలపడనున్నాయి. అభిషేక్ శర్మ, ట్రావిస్‌ హెడ్‌ల విధ్వంసక బ్యాటింగ్‌తో ఐపీఎల్‌లో అత్యధిక స్కోర్లు (287/3, 277/3) సాధించిన సన్‌రైజర్స్‌, భువనేశ్వర్‌-నటరాజన్-కమిన్స్‌ల ప్రభావవంతమైన బౌలింగ్‌తో బలంగా ఉంది. నరైన్, శ్రేయస్, రాణా, రసెల్‌లతో కోల్‌కతా బ్యాటింగ్‌ దుర్భేద్యం. వరుణ్‌ చక్రవర్తి, హర్షిత్‌ రాణాల స్పిన్ కోల్‌కతా ఆయుధం. 26 ఎదుర్కోలుల్లో కోల్‌కతాదే పైచేయి (17-7). బ్యాటింగ్‌కు అనుకూలమైన పిచ్‌పై రసవత్తర పోరు జరగనుంది. విజేత నేరుగా ఫైనల్‌కు చేరుతుంది.

3. Entertainment:
Article:
ప్రముఖ దర్శకుడు ఎస్.ఎస్. రాజమౌళి తన తదుపరి చిత్రాన్ని ప్రకటించారు. ఈ సినిమాలో బాలీవుడ్ స్టార్ హృతిక్ రోషన్ మరియు తెలుగు స్టార్ మహేష్ బాబు ప్రధాన పాత్రలు పోషిస్తారు. ఈ చిత్రం ఒక అంతర్జాతీయ స్పై థ్రిల్లర్ అని రాజమౌళి తెలిపారు. "ఇది నా కెరీర్‌లో సరికొత్త ప్రయత్నం. ప్రేక్షకులకు ఒక కొత్త అనుభూతిని అందించాలని ఆశిస్తున్నాను," అని ఆయన అన్నారు. సినిమా షూటింగ్ వచ్చే నెలలో ప్రారంభం కానుంది, మరియు 2025 సంవత్సరంలో విడుదల చేయాలని యోచిస్తున్నారు. ఈ చిత్రానికి ఎం.ఎం. కీరవాణి సంగీతం అందిస్తారు. ఈ సినిమా కోసం ప్రపంచవ్యాప్తంగా వివిధ ప్రదేశాలలో చిత్రీకరణ జరుగుతుందని తెలుస్తోంది. ఇందులో అత్యాధునిక వీఎఫ్ఎక్స్ మరియు స్టంట్ సీక్వెన్సులు ఉంటాయని సమాచారం. ఇప్పటికే ఈ ప్రాజెక్ట్‌పై అంచనాలు భారీగా పెరిగాయి. ఈ చిత్రంతో రాజమౌళి అంతర్జాతీయ మార్కెట్‌లో మరింత గట్టి పట్టు సాధించాలని లక్ష్యంగా పెట్టుకున్నట్లు సమాచారం.

హెడ్‌లైన్: రాజమౌళి-హృతిక్-మహేష్ కాంబోతో స్పై థ్రిల్లర్!

సారాంశం: రాజమౌళి కొత్త చిత్రంలో హృతిక్ రోషన్, మహేష్ బాబు నటిస్తారు. ఇది అంతర్జాతీయ స్పై థ్రిల్లర్. 2025లో విడుదల కానున్న ఈ చిత్రానికి కీరవాణి సంగీతం. ప్రపంచవ్యాప్తంగా షూటింగ్, అత్యాధునిక వీఎఫ్ఎక్స్‌తో తెరకెక్కనుంది.

Article:
{article}

Respond in this format:
హెడ్‌లైన్: [Your engaging short Telugu headline]
సారాంশం: [Your concise Telugu summary with all critical information]

Remember: Ensure that all information in the headline and summary is directly derived from the given article. Do not introduce any information that is not present in the original text. Retain and accurately represent all numbers, statistics, and vital details from the original article in the summary.

Finally make sure that title matches the summary """


TELUGU_CHECK_PROMPT = """
Please check the following Telugu news headline and summary for grammar, meaning, sentence formation and spelling errors. Also check if the news headline matches the summary.
If there are any mistakes, provide the corrected version. If there are no mistakes, 
return the original text unchanged.

Telugu headline: {headline}
Telugu summary: {summary}

Please return your response in the following format only:
Corrected Telugu headline: [corrected headline]
Corrected Telugu summary: [corrected summary]
"""
