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

HOOK_EXTRACTION_PROMPT = """Extract ONLY HIGH-SIGNAL, BUSINESS-RELEVANT personalization hooks from this prospect data.

Data:
{prospect_data}

PRIORITIZE (extract these if present):
- Role changes (promotions, new positions, career transitions)
- Scaling signals (team growth, company expansion)
- Product launches (shipped new features, released products)
- Hiring spikes (actively recruiting, growing team)
- Infrastructure upgrades (migrations, tech stack changes)
- Tech stack mentions (specific tools, frameworks, platforms)
- Performance complaints (speed issues, scaling pain points)
- Public pain points (mentioned challenges, struggles)
- Recent achievements with business impact (not generic awards)

AVOID (discard these):
- Personal hobbies (unless directly business-relevant)
- Generic achievements without context
- Motivational posts or quotes
- Generic interests (reading, traveling, etc.)
- Social activities unrelated to work

CRITICAL RULE:
Discard hooks that cannot naturally connect to a business product or service.

Return a list of the most relevant BUSINESS-FOCUSED hooks for cold outreach."""

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
- Style: Sharp, confident, insight-led (like an industry insider)
- Length: 150-200 words
- Include: Subject line + body
- Structure: Hook -> Personalized insight -> Value proposition -> Soft CTA
- Tone: Write like a sharp industry insider who understands their business
- Avoid sounding like a marketing team
- Avoid generic SaaS language
- Prioritize insight over politeness
- Be confident, not apologetic

CRITICAL ANTI-HALLUCINATION RULES:
1. ONLY use details explicitly provided in PROSPECT DATA above
2. DO NOT invent competitions, achievements, or activities not mentioned
3. DO NOT use placeholders like [project name] or [Your Name]
4. If GitHub projects are listed, use their ACTUAL names
5. Product info must match PRODUCT/SERVICE INFORMATION section exactly
6. DO NOT fabricate mutual connections or events
7. If no specific detail exists, use broader but honest language
8. DO NOT infer pain points unless directly supported by data
9. If no pain point exists, use curiosity-driven messaging instead
10. Never assume struggles, challenges, or problems not explicitly mentioned

PERSONALIZATION STRATEGY:
- Open with something that stops scanning behavior (pattern interrupt)
- Avoid generic openings like "Hope you're well" or "Came across your profile"
- Start with their most relevant BUSINESS achievement or activity from hooks
- Connect their actual skills/projects to the product naturally
- Show how the product solves THEIR specific pain points (only if data supports it)
- If no clear pain point: use curiosity-driven or insight-led messaging
- Keep it authentic and conversational
- IF PROSPECT ROLE DOESN'T MATCH PRODUCT (e.g., engineer for sales tool):
  * Focus on HOW they might indirectly benefit (e.g., recruiting, partnerships)
  * OR acknowledge the mismatch and suggest relevant use cases
  * Don't force a connection that doesn't exist naturally

DELIVERABILITY PROTECTION:
Avoid spam trigger phrases:
- revolutionize, cutting edge, guaranteed, limited time, exclusive offer, act now
- game-changer, breakthrough, innovative solution, transform your business
- best in class, world-class, industry-leading, award-winning
Use natural sentence variation and avoid overly promotional language.

FORMATTING:
- NO emojis (keep it professional)
- Plain text only

{reference}

Language: {language}

OUTPUT FORMAT (CRITICAL):
- Start DIRECTLY with "Subject:" (no markdown, no bold)
- Then blank line
- Then email body
- NO introductory phrases like "Here's the email" or "Here is..."
- NO explanatory notes about what you did
- NO meta-commentary about tone or changes
- NO closing statements
- Just the email itself, nothing else

Example format:
Subject: Your subject here

Hey [Name],

[Body content...]

Cheers,
[Signature]

Generate the email now (output format exactly as shown above):"""

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
- Style: Sharp, direct, conversational (like texting an industry peer)
- Length: 300-400 characters (brief!)
- Structure: Pattern interrupt hook -> Quick insight -> Simple CTA
- Tone: Confident and casual (not polite/formal)
- Can use 1-2 relevant emojis
- NO formal language or marketing speak
- Get to the point fast
- Feel like a message from a real person who knows their industry
- IF prospect role doesn't match product audience, find a creative angle or skip the pitch

CRITICAL RULES:
1. ONLY use real details from PROSPECT DATA
2. NO placeholders or invented achievements
3. Use actual project/skill names if mentioned
4. Product must match PRODUCT/SERVICE INFORMATION
5. DO NOT infer pain points unless directly supported by data
6. Avoid spam triggers: revolutionize, cutting edge, guaranteed, limited time, act now

{reference}

Language: {language}

OUTPUT FORMAT (CRITICAL):
- Start DIRECTLY with the message
- NO introductory phrases like "Here's the message" or "Here is..."
- NO explanatory notes
- NO meta-commentary
- Just the WhatsApp message itself

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
- Include a clear CTA (e.g., "Interested?", "Quick chat?", "Worth a look?")
- Can use 1-2 emojis if appropriate
- NO fluff or filler words
- Every word counts
- Use ONLY real details, no placeholders like [link] or [CTA]
- NO brackets or placeholder text - write complete message

Language: {language}

OUTPUT FORMAT (CRITICAL):
- Start DIRECTLY with the SMS message
- NO introductory phrases
- NO explanations or notes
- NO placeholders in brackets like [link] or [CTA]
- Just the complete text message (max 160 chars)

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
- Style: Sharp professional (industry insider, not vendor)
- Length: 200-250 words
- Reference their actual LinkedIn activity/posts if available
- Show you're in the same professional community
- Build credibility before mentioning product
- Tone: Confident peer, not salesperson
- IF prospect role doesn't naturally fit product, find indirect value or acknowledge it
- Avoid spam triggers and promotional language
- Insight-focused, not pitchy
- Professional but confident (avoid being overly polite)
- Pattern interrupt opening for technical personas
- More traditional opening for executive personas
- NO emojis (professional platform)

CRITICAL RULES:
1. ONLY use details from PROSPECT DATA
2. NO invented competitions, awards, or activities
3. Use actual GitHub project names if mentioned
4. NO placeholders like [Your Name]
5. Product must match PRODUCT/SERVICE INFORMATION
6. Be honest - if limited data, be broader but authentic
7. DO NOT infer pain points unless directly supported by data
8. If no pain point: use curiosity-driven or insight-led messaging
9. Avoid spam triggers: revolutionize, cutting edge, guaranteed, limited time, exclusive offer

{reference}

Language: {language}

OUTPUT FORMAT (CRITICAL):
- Start DIRECTLY with the message (e.g., "Hey [Name],")
- NO introductory phrases like "Here's the message"
- NO explanatory notes about what you changed
- NO meta-commentary
- Just the LinkedIn DM itself

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
- Style: Casual, authentic, confident (not salesy)
- Length: 150-200 words
- Tone: Like messaging a peer, not a prospect
- Reference their actual content/posts if available
- Be genuine and human
- Can use 2-3 relevant emojis naturally
- NO corporate speak or marketing language
- Build connection first, business second
- Pattern interrupt opening (avoid "came across your profile")

CRITICAL RULES:
1. ONLY use real details from PROSPECT DATA
2. NO invented achievements or activities
3. Use actual project names if listed
4. NO placeholders
5. Product must match PRODUCT/SERVICE INFORMATION
6. DO NOT infer pain points unless directly supported by data
7. Avoid spam triggers: revolutionize, guaranteed, limited time, exclusive

Language: {language}

OUTPUT FORMAT (CRITICAL):
- Start DIRECTLY with the message
- NO introductory phrases like "Here's the DM"
- NO explanatory notes
- NO meta-commentary
- Just the Instagram message itself

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

OUTPUT FORMAT (CRITICAL):
- Start DIRECTLY with the regenerated message
- NO introductory phrases like "Here's the updated..."
- NO explanatory notes about changes made
- NO meta-commentary
- Just the message itself

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
