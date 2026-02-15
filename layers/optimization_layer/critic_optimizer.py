"""
Critic Optimizer - Persona-aware automatic optimization for response rates
"""

# Persona-specific critic prompts
CRITIC_PROMPTS = {
    'technical': """You are a harsh critic optimizing outreach for technical audiences.

ORIGINAL:
{content}

PROSPECT: {role} at {company}

RULES FOR TECHNICAL PERSONAS:
- Remove ALL marketing fluff
- Keep technical terms (they appreciate precision)  
- Be direct and data-driven
- Cut 20-30% while keeping personalization
- No corporate speak
- Sound like a sharp technical peer, not a vendor
- DO NOT infer pain points unless data supports it
- Avoid spam triggers (revolutionize, cutting edge, guaranteed)

CHANNEL: {channel} | Max length: {max_length}

OUTPUT FORMAT (CRITICAL):
- Start DIRECTLY with the improved message
- NO phrases like "Here's the rewritten..." or "Here is..."
- NO explanations of what you changed
- NO notes about tone, style, or improvements made
- NO meta-commentary
- Just the improved message itself, nothing before or after
- If email: Start with "Subject:" (no bold/markdown)
- If other channel: Start with first word of message

Rewrite for maximum response rate (output the message directly, no commentary):""",

    'executive': """You are a harsh critic optimizing outreach for busy executives.

ORIGINAL:
{content}

PROSPECT: {role} at {company}

RULES FOR EXECUTIVES (They have 30 seconds):
- First sentence = value (no fluff)
- Cut 30-40% ruthlessly
- Crystal clear ROI/benefit
- Shorter sentences, active voice
- Make it scannable
- Sound confident and sharp, not polite
- DO NOT infer pain points unless data supports it
- Avoid spam triggers and overly promotional language

CHANNEL: {channel} | Max length: {max_length}

OUTPUT FORMAT (CRITICAL):
- Start DIRECTLY with the improved message
- NO phrases like "Here's the rewritten..." or "Here is..."
- NO explanations of what you changed
- NO notes about tone, style, or improvements made
- NO meta-commentary
- Just the improved message itself, nothing before or after
- If email: Start with "Subject:" (no bold/markdown)
- If other channel: Start with first word of message

Rewrite for maximum response rate (output the message directly, no commentary):""",

    'casual': """You are a harsh critic optimizing outreach for casual/creative audiences.

ORIGINAL:
{content}

PROSPECT: {role} at {company}

RULES FOR CASUAL PERSONAS:
- Remove ALL corporate language
- Make it conversational and authentic
- Be human, not professional-robot
- Keep personality
- Sound like a peer, not a salesperson
- Sharp and confident, not apologetic
- DO NOT infer pain points unless data supports it
- Pattern interrupt opening (avoid generic "came across your profile")

CHANNEL: {channel} | Max length: {max_length}

OUTPUT FORMAT (CRITICAL):
- Start DIRECTLY with the improved message
- NO phrases like "Here's the rewritten..." or "Here is..."
- NO explanations of what you changed
- NO notes about tone, style, or improvements made
- NO meta-commentary
- Just the improved message itself, nothing before or after
- If email: Start with "Subject:" (no bold/markdown)
- If other channel: Start with first word of message

Rewrite for maximum response rate (output the message directly, no commentary):""",

    'formal': """You are a harsh critic optimizing outreach for formal/professional audiences.

ORIGINAL:
{content}

PROSPECT: {role} at {company}

RULES FOR FORMAL PERSONAS:
- Maintain professional tone (but confident, not timid)
- Clear structure (intro, value, ask)
- Cut fluff but keep courtesy
- Reduce by 20-25%
- Complete sentences, no slang
- DO NOT infer pain points unless data supports it
- Avoid spam triggers and promotional language

CHANNEL: {channel} | Max length: {max_length}

OUTPUT FORMAT (CRITICAL):
- Start DIRECTLY with the improved message
- NO phrases like "Here's the rewritten..." or "Here is..."
- NO explanations of what you changed
- NO notes about tone, style, or improvements made
- NO meta-commentary
- Just the improved message itself, nothing before or after
- If email: Start with "Subject:" (no bold/markdown)
- If other channel: Start with first word of message

Rewrite for maximum response rate (output the message directly, no commentary):"""
}

# Channel max lengths
CHANNEL_LENGTHS = {
    'email': '200 words',
    'whatsapp': '400 chars',
    'sms': '160 chars',
    'linkedin': '250 words',
    'instagram': '200 words'
}


def clean_llm_output(content):
    """
    Remove common LLM meta-commentary that might slip through despite prompt instructions
    
    Args:
        content: str - LLM output
    
    Returns:
        str: cleaned content
    """
    import re
    
    # Remove common introductory phrases (more comprehensive patterns)
    intro_patterns = [
        r"^Here'?s?\s+(the\s+)?(rewritten\s+|updated\s+|improved\s+)?.*?:?\s*\n*",
        r"^Here\s+is\s+(the\s+)?(rewritten\s+|updated\s+|improved\s+)?.*?:?\s*\n*",
        r"^I've\s+rewritten.*?:?\s*\n*",
        r"^I\s+removed.*?:?\s*\n*",
        r"^the\s+rewritten\s+.*?:?\s*\n+",
        r"^rewritten\s+.*?:?\s*\n+"
    ]
    
    for pattern in intro_patterns:
        content = re.sub(pattern, "", content, flags=re.IGNORECASE | re.MULTILINE)
    
    # Remove markdown bold from Subject line and other formatting
    content = re.sub(r'\*\*Subject:\*\*', 'Subject:', content)
    content = re.sub(r'\*\*Body:\*\*', '', content)
    
    # Remove placeholder text in brackets (e.g., [CTA link], [Your Name], [link])
    content = re.sub(r'\[CTA link\]', 'Reply?', content, flags=re.IGNORECASE)
    content = re.sub(r'\[link\]', '', content, flags=re.IGNORECASE)
    content = re.sub(r'\[Your Name\]', '', content, flags=re.IGNORECASE)
    content = re.sub(r'\[.*?\]', '', content)  # Remove any remaining bracketed placeholders
    
    # Remove trailing explanations (paragraphs starting with common meta-phrases)
    lines = content.split('\n')
    cleaned_lines = []
    found_meta = False
    
    meta_starters = [
        'this rewritten',
        'this updated',
        'i removed',
        'i made',
        'i changed',
        'note:',
        'the tone',
        'the style'
    ]
    
    for line in lines:
        line_lower = line.strip().lower()
        if any(line_lower.startswith(phrase) for phrase in meta_starters):
            found_meta = True
            break
        if not found_meta:
            cleaned_lines.append(line)
    
    content = '\n'.join(cleaned_lines).strip()
    
    # Remove parenthetical notes at the end
    content = re.sub(r'\(Note:.*?\)\s*$', '', content, flags=re.IGNORECASE | re.DOTALL)
    
    return content


def apply_critic_pass(content, channel, prospect_data, persona, config, llm_generate_func):
    """
    Apply persona-aware critic optimization (silent, automatic)
    
    Args:
        content: str - original content
        channel: str - channel name
        prospect_data: dict - prospect info
        persona: dict - persona analysis
        config: dict - LLM config
        llm_generate_func: function - LLM generator
    
    Returns:
        str: optimized content (or original if error)
    """
    try:
        style = persona.get('communication_style', 'formal')
        
        # Get appropriate critic prompt
        prompt_template = CRITIC_PROMPTS.get(style, CRITIC_PROMPTS['formal'])
        
        # Build prompt
        prompt = prompt_template.format(
            content=content,
            role=prospect_data.get('title') or prospect_data.get('role') or 'Professional',
            company=prospect_data.get('company') or 'their company',
            channel=channel.upper(),
            max_length=CHANNEL_LENGTHS.get(channel, '200 words')
        )
        
        # Generate optimized version
        optimized = llm_generate_func(prompt, config, max_tokens=600)
        
        # Clean up any meta-commentary that might have slipped through
        optimized = clean_llm_output(optimized)
        
        # Calculate improvement
        original_len = len(content)
        optimized_len = len(optimized)
        reduction = ((original_len - optimized_len) / original_len * 100) if original_len > 0 else 0
        
        print(f"   ✓ Optimized ({reduction:.0f}% clearer)")
        
        return optimized
        
    except Exception as e:
        print(f"   ! Optimization skipped: {str(e)}")
        return content  # Return original on error
