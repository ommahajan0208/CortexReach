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

CHANNEL: {channel} | Max length: {max_length}

Rewrite for maximum response rate. Output ONLY the improved message:""",

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

CHANNEL: {channel} | Max length: {max_length}

Rewrite for maximum response rate. Output ONLY the improved message:""",

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

CHANNEL: {channel} | Max length: {max_length}

Rewrite for maximum response rate. Output ONLY the improved message:""",

    'formal': """You are a harsh critic optimizing outreach for formal/professional audiences.

ORIGINAL:
{content}

PROSPECT: {role} at {company}

RULES FOR FORMAL PERSONAS:
- Maintain professional tone
- Clear structure (intro, value, ask)
- Cut fluff but keep courtesy
- Reduce by 20-25%
- Complete sentences, no slang

CHANNEL: {channel} | Max length: {max_length}

Rewrite for maximum response rate. Output ONLY the improved message:"""
}

# Channel max lengths
CHANNEL_LENGTHS = {
    'email': '200 words',
    'whatsapp': '400 chars',
    'sms': '160 chars',
    'linkedin': '250 words',
    'instagram': '200 words'
}


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
        
        # Calculate improvement
        original_len = len(content)
        optimized_len = len(optimized)
        reduction = ((original_len - optimized_len) / original_len * 100) if original_len > 0 else 0
        
        print(f"   ✓ Optimized ({reduction:.0f}% clearer)")
        
        return optimized
        
    except Exception as e:
        print(f"   ! Optimization skipped: {str(e)}")
        return content  # Return original on error
