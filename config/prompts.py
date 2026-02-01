"""
Channel-specific prompts for content generation
Each channel has unique style, length, and tone requirements
"""

# Analysis prompts
PERSONA_ANALYSIS_PROMPT = """Analyze this prospect data and identify their persona:

Data:
{prospect_data}

Identify:
1. Communication style (formal/casual/technical)
2. Key interests and expertise areas
3. Likely pain points based on role and activity
4. Personality indicators

Return a concise analysis focusing on what matters for personalized outreach."""

HOOK_EXTRACTION_PROMPT = """Extract personalization hooks from this prospect data:

Data:
{prospect_data}

Find specific, actionable hooks such as:
- Recent activities or posts
- Shared interests or experiences
- Technical expertise or tools they use
- Company challenges or initiatives
- Career achievements or transitions

Return a list of the most relevant hooks for cold outreach."""

# Email generation prompt (Professional, structured, 150-200 words)
EMAIL_PROMPT = """Generate a hyper-personalized cold email for this prospect.

PROSPECT DATA:
{prospect_data}

PERSONA ANALYSIS:
{persona}

PERSONALIZATION HOOKS:
{hooks}

{company_context}

REQUIREMENTS:
- Style: Professional and structured
- Length: 150-200 words
- Include: Subject line + body
- Structure: Hook -> Personalized insight -> Value proposition -> Soft CTA
- Tone: Respectful, value-focused, not salesy
- NO generic templates or buzzwords
- Reference SPECIFIC details from their profile
- Show genuine research
- Be conversational yet professional

{reference}

Language: {language}

Format:
SUBJECT: [subject line]

BODY:
[email body]"""

# WhatsApp generation prompt (Conversational, brief, ~300-400 chars)
WHATSAPP_PROMPT = """Generate a hyper-personalized WhatsApp message for this prospect.

PROSPECT DATA:
{prospect_data}

PERSONA ANALYSIS:
{persona}

PERSONALIZATION HOOKS:
{hooks}

{company_context}

REQUIREMENTS:
- Style: Conversational and friendly
- Length: 300-400 characters (brief!)
- Structure: Quick hook -> Value mention -> Simple CTA
- Tone: Casual but respectful
- Can use 1-2 relevant emojis
- NO formal language
- Get to the point fast
- Feel like a message from a real person

{reference}

Language: {language}

Generate ONLY the message text:"""

# SMS generation prompt (Ultra-short, punchy, max 160 chars)
SMS_PROMPT = """Generate a hyper-personalized SMS for this prospect.

PROSPECT DATA:
{prospect_data}

PERSONALIZATION HOOKS:
{hooks}

REQUIREMENTS:
- Style: Ultra-concise and punchy
- Length: Maximum 160 characters (strict!)
- Must include one personalized element
- Include a clear CTA
- NO fluff or filler words
- Every word counts

Language: {language}

Generate ONLY the SMS text:"""

# LinkedIn DM prompt (Professional-casual, value-focused, ~200-250 words)
LINKEDIN_PROMPT = """Generate a hyper-personalized LinkedIn direct message for this prospect.

PROSPECT DATA:
{prospect_data}

PERSONA ANALYSIS:
{persona}

PERSONALIZATION HOOKS:
{hooks}

{company_context}

REQUIREMENTS:
- Style: Professional-casual (LinkedIn native tone)
- Length: 200-250 words
- Reference their LinkedIn activity/posts if available
- Show you're in the same professional community
- Value-focused, not pitchy
- Mention mutual interests or connections if relevant
- Professional but not stiff

{reference}

Language: {language}

Generate the LinkedIn message:"""

# Instagram DM prompt (Casual, friendly, visual-oriented, ~150-200 words)
INSTAGRAM_PROMPT = """Generate a hyper-personalized Instagram direct message for this prospect.

PROSPECT DATA:
{prospect_data}

PERSONA ANALYSIS:
{persona}

PERSONALIZATION HOOKS:
{hooks}

REQUIREMENTS:
- Style: Casual, friendly, and authentic
- Length: 150-200 words
- Tone: Like messaging a potential friend
- Reference their content/posts if available
- Be genuine and human
- Can use emojis naturally
- NO corporate speak
- Build connection first, business second

Language: {language}

Generate the Instagram DM:"""

# Regeneration prompt (keeps tone but applies user modifications)
REGENERATION_PROMPT = """Regenerate this {channel} message with the user's requested changes while maintaining the original tone and style.

ORIGINAL CONTENT:
{original_content}

USER MODIFICATIONS REQUESTED:
{user_modifications}

CHANNEL REQUIREMENTS ({channel}):
{channel_requirements}

INSTRUCTIONS:
- Keep the same tone, style, and personalization level
- Apply ONLY the specific changes the user requested
- Maintain the same structure unless user asks to change it
- Keep all personalization hooks unless user says otherwise
- Preserve the channel-specific format

Language: {language}

Generate the updated {channel} message:"""

# Channel requirements for regeneration
CHANNEL_REQUIREMENTS = {
    "email": "Professional, structured, 150-200 words, includes subject line",
    "whatsapp": "Conversational, brief, 300-400 characters, casual tone",
    "sms": "Ultra-short, max 160 characters, punchy",
    "linkedin": "Professional-casual, 200-250 words, LinkedIn-native tone",
    "instagram": "Casual, friendly, 150-200 words, authentic and human"
}


def get_channel_prompt(channel):
    """Get the appropriate prompt for a channel"""
    prompts = {
        "email": EMAIL_PROMPT,
        "whatsapp": WHATSAPP_PROMPT,
        "sms": SMS_PROMPT,
        "linkedin": LINKEDIN_PROMPT,
        "instagram": INSTAGRAM_PROMPT
    }
    return prompts.get(channel.lower(), EMAIL_PROMPT)


def get_regeneration_prompt():
    """Get the regeneration prompt"""
    return REGENERATION_PROMPT


def get_channel_requirements(channel):
    """Get channel-specific requirements"""
    return CHANNEL_REQUIREMENTS.get(channel.lower(), "")
