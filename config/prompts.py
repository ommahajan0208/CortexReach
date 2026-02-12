"""
Channel-specific prompts for content generation
Each channel has unique style, length, and tone requirements
"""

# Analysis prompts
PERSONA_ANALYSIS_PROMPT = """Analyze this prospect data and determine their communication style.

Data:
{prospect_data}

Based on their role, title, and professional context, return ONLY ONE of these communication styles:
- executive (short, high-value, decision-focused - for C-level, VPs, Directors, Founders)
- technical (logical, detailed, data-driven - for engineers, developers, technical specialists)
- friendly (warm, personalized, human - for creative roles, community-focused professionals)
- formal (professional, structured, low slang - for traditional corporate roles, consultants)
- skeptical (low-pressure, trust-building - for privacy-conscious or cautious professionals)

Return ONLY the style name, nothing else. Just one word: executive, technical, friendly, formal, or skeptical."""

PERSONA_TYPE_PROMPT = """Analyze this prospect data and determine their persona type.

Data:
{prospect_data}

Based on their activities, interests, role, and professional behavior, return ONLY ONE of these persona types:
- innovator (early adopters, tech enthusiasts, loves new solutions and cutting-edge tools)
- builder (makers, creators, hands-on developers who build and ship products)
- analyst (data-driven, researchers, strategic thinkers who deep-dive into problems)
- leader (managers, executives, team leads focused on people and organizational growth)
- specialist (deep experts in specific domains, focused on mastery)
- entrepreneur (founders, business builders, growth-focused, opportunity seekers)

Return ONLY the persona type name, nothing else. Just one word: innovator, builder, analyst, leader, specialist, or entrepreneur."""

KEY_INTERESTS_PROMPT = """Analyze this prospect data and identify their top 3 key interests or focus areas.

Data:
{prospect_data}

Based on their skills, projects, activities, bio, and professional context, identify the 3 most relevant interests or focus areas that would be valuable for personalized outreach.

Return ONLY a comma-separated list of 3 interests, ordered from MOST relevant to LEAST relevant. No explanations, no numbering, just: interest1, interest2, interest3

Example formats:
- AI/ML, Cloud Infrastructure, DevOps
- Product Design, User Research, SaaS Growth
- Data Analytics, Python, Business Intelligence"""

HOOK_EXTRACTION_PROMPT = """Extract personalization hooks from this prospect data:

Data:
{prospect_data}

Find specific, actionable hooks such as:
- Recent activities or posts
- Shared interests or experiences
- Technical expertise or tools they use
- Company challenges or initiatives
- Career achievements or transitions

Return ONLY a comma-separated list of 3-5 personalization hooks, ordered from MOST relevant to LEAST relevant for cold outreach. No explanations, no numbering, just the hooks separated by commas.

Example format:
Recently launched AI chatbot project, Uses Python and React extensively, Passionate about developer tools"""

# Email generation prompt (Professional, structured, 150-200 words)
EMAIL_PROMPT = """Generate a hyper-personalized cold email for this prospect.

PROSPECT DATA:
{prospect_data}

PERSONA ANALYSIS:
{persona}

PERSONALIZATION HOOKS:
{hooks}

PRODUCT/SERVICE INFORMATION:
{product_info}

{company_context}

REQUIREMENTS:
- Style: Professional and structured
- Length: 150-200 words
- Include: Subject line + body
- Structure: Hook -> Personalized insight -> Value proposition -> Soft CTA
- Tone: Respectful, value-focused, not salesy

CRITICAL ANTI-HALLUCINATION RULES:
1. ONLY use details explicitly provided in PROSPECT DATA above
2. DO NOT invent competitions, achievements, or activities not mentioned
3. DO NOT use placeholders like [project name] or [Your Name]
4. If GitHub projects are listed, use their ACTUAL names
5. Product info must match PRODUCT/SERVICE INFORMATION section exactly
6. DO NOT fabricate mutual connections or events
7. If no specific detail exists, use broader but honest language

PERSONALIZATION STRATEGY:
- Start with their most relevant achievement or activity from hooks
- Connect their actual skills/projects to the product naturally
- Show how the product solves THEIR specific pain points
- Keep it authentic and conversational

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

PRODUCT/SERVICE INFORMATION:
{product_info}

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

CRITICAL RULES:
1. ONLY use real details from PROSPECT DATA
2. NO placeholders or invented achievements
3. Use actual project/skill names if mentioned
4. Product must match PRODUCT/SERVICE INFORMATION

{reference}

Language: {language}

Generate ONLY the message text:"""

# SMS generation prompt (Ultra-short, punchy, max 160 chars)
SMS_PROMPT = """Generate a hyper-personalized SMS for this prospect.

PROSPECT DATA:
{prospect_data}

PERSONALIZATION HOOKS:
{hooks}

PRODUCT/SERVICE:
{product_info}

REQUIREMENTS:
- Style: Ultra-concise and punchy
- Length: Maximum 160 characters (strict!)
- Must include one personalized element from prospect data
- Include a clear CTA
- NO fluff or filler words
- Every word counts
- Use ONLY real details, no placeholders

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

PRODUCT/SERVICE INFORMATION:
{product_info}

{company_context}

REQUIREMENTS:
- Style: Professional-casual (LinkedIn native tone)
- Length: 200-250 words
- Reference their actual LinkedIn activity/posts if available
- Show you're in the same professional community
- Value-focused, not pitchy
- Professional but not stiff

CRITICAL RULES:
1. ONLY use details from PROSPECT DATA
2. NO invented competitions, awards, or activities
3. Use actual GitHub project names if mentioned
4. NO placeholders like [Your Name]
5. Product must match PRODUCT/SERVICE INFORMATION
6. Be honest - if limited data, be broader but authentic

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

PRODUCT/SERVICE INFORMATION:
{product_info}

REQUIREMENTS:
- Style: Casual, friendly, and authentic
- Length: 150-200 words
- Tone: Like messaging a potential friend
- Reference their actual content/posts if available
- Be genuine and human
- Can use emojis naturally
- NO corporate speak
- Build connection first, business second

CRITICAL RULES:
1. ONLY use real details from PROSPECT DATA
2. NO invented achievements or activities
3. Use actual project names if listed
4. NO placeholders
5. Product must match PRODUCT/SERVICE INFORMATION

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
