"""
LLM Interface - Communication with offline LLM
"""

import requests
import re


def clean_llm_output(content):
    """
    Remove common LLM meta-commentary that might slip through despite prompt instructions
    
    Args:
        content: str - LLM output
    
    Returns:
        str: cleaned content
    """
    # Remove common introductory phrases
    intro_patterns = [
        r"^Here'?s?\s+(the\s+)?(rewritten\s+|updated\s+|improved\s+)?\w+:?\s*\n*",
        r"^Here\s+is\s+(the\s+)?(rewritten\s+|updated\s+|improved\s+)?\w+:?\s*\n*",
        r"^I've\s+rewritten.*?:?\s*\n*",
        r"^I\s+removed.*?:?\s*\n*"
    ]
    
    for pattern in intro_patterns:
        content = re.sub(pattern, "", content, flags=re.IGNORECASE | re.MULTILINE)
    
    # Remove markdown bold from Subject line
    content = re.sub(r'\*\*Subject:\*\*', 'Subject:', content)
    content = re.sub(r'\*\*Body:\*\*', '', content)
    
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


def generate_with_llm(prompt, config, max_tokens=500):
    """
    Generate text using offline LLM
    
    Args:
        prompt: str - prompt to send to LLM
        config: dict - LLM configuration
        max_tokens: int - maximum tokens to generate
    
    Returns:
        str: generated text
    """
    provider = config.get('provider', 'ollama')
    
    if provider == 'ollama':
        return generate_with_ollama(prompt, config, max_tokens)
    else:
        raise Exception(f"Unsupported LLM provider: {provider}")


def generate_with_ollama(prompt, config, max_tokens):
    """Generate using Ollama"""
    url = f"{config['api_url']}/api/generate"
    
    payload = {
        'model': config['model_name'],
        'prompt': prompt,
        'temperature': config.get('temperature', 0.7),
        'stream': False,
        'options': {
            'num_predict': max_tokens
        }
    }
    
    try:
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()
        
        result = response.json()
        return result.get('response', '').strip()
        
    except requests.Timeout:
        raise Exception("LLM request timed out. The model might be too slow or overloaded.")
    except requests.RequestException as e:
        raise Exception(f"LLM request failed: {str(e)}")
    except Exception as e:
        raise Exception(f"Error generating with LLM: {str(e)}")


def generate_for_channel(prospect_data, persona, hooks, company_context, reference, 
                        channel, config):
    """
    Generate content for a specific channel
    
    Args:
        prospect_data: dict
        persona: dict
        hooks: list
        company_context: dict
        reference: str or None
        channel: str - channel name
        config: dict - LLM configuration
    
    Returns:
        str: generated content
    """
    from config.prompts import get_channel_prompt
    from layers.context_layer.reference_builder import format_reference_for_prompt
    from layers.generation_layer.product_config import get_default_product_info, format_product_for_prompt
    
    print(f"\n[GENERATION] Generating {channel.upper()} content...")
    
    # Get channel-specific prompt
    prompt_template = get_channel_prompt(channel)
    
    # Format data for prompt
    prospect_summary = format_prospect_for_prompt(prospect_data)
    persona_summary = format_persona_for_prompt(persona)
    hooks_summary = format_hooks_for_prompt(hooks)
    company_summary = format_company_context_for_prompt(company_context)
    reference_text = format_reference_for_prompt(reference)
    
    # Get product info (silently use CortexReach default)
    product_info = get_default_product_info()
    product_summary = format_product_for_prompt(product_info)
    
    # Build final prompt
    prompt = prompt_template.format(
        prospect_data=prospect_summary,
        persona=persona_summary,
        hooks=hooks_summary,
        company_context=company_summary,
        reference=reference_text,
        product_info=product_summary,
        language=config['language']
    )
    
    # Generate
    max_tokens = get_max_tokens_for_channel(channel)
    content = generate_with_llm(prompt, config, max_tokens)
    
    # Clean up any meta-commentary from the LLM
    content = clean_llm_output(content)
    
    print(f"{channel.upper()} content generated ({len(content)} chars)")
    
    return content


def get_max_tokens_for_channel(channel):
    """Get appropriate max tokens for each channel"""
    tokens = {
        'email': 600,
        'whatsapp': 300,
        'sms': 100,
        'linkedin': 600,
        'instagram': 500
    }
    return tokens.get(channel.lower(), 500)


def format_prospect_for_prompt(data):
    """Format prospect data for prompt with comprehensive details"""
    lines = []
    
    # Basic info
    if data.get('name'):
        lines.append(f"Name: {data['name']}")
    if data.get('role'):
        lines.append(f"Role: {data['role']}")
    if data.get('company'):
        lines.append(f"Company: {data['company']}")
    if data.get('bio'):
        lines.append(f"Bio: {data['bio']}")
    
    # GitHub projects (ACTUAL NAMES)
    if data.get('github_projects'):
        project_names = [p['name'] for p in data['github_projects'][:3]]
        lines.append(f"GitHub Projects: {', '.join(project_names)}")
        for proj in data['github_projects'][:2]:
            if proj.get('description'):
                lines.append(f"  - {proj['name']}: {proj['description']}")
    
    # Languages/Skills
    if data.get('github_languages'):
        lines.append(f"Technical Skills: {', '.join(data['github_languages'])}")
    elif data.get('skills'):
        lines.append(f"Skills: {', '.join(data['skills'][:5])}")
    
    # Recent activity
    if data.get('recent_activity'):
        lines.append(f"Recent Achievement: {data['recent_activity'][0][:200]}")
    
    # Twitter interests
    if data.get('x_bio'):
        lines.append(f"Interests: {data['x_bio'][:150]}")
    
    return '\n'.join(lines) if lines else "Limited data available"


def format_persona_for_prompt(persona):
    """Format persona for prompt"""
    if not persona:
        return "Professional"
    return f"Style: {persona.get('communication_style', 'professional')}\n{persona.get('raw_analysis', '')[:300]}"


def format_hooks_for_prompt(hooks):
    """Format hooks for prompt with full context"""
    if not hooks:
        return "No specific hooks available - keep message general and value-focused"
    
    hook_lines = []
    for i, hook in enumerate(hooks[:5], 1):
        hook_text = hook['hook_text']
        hook_type = hook.get('type', 'general')
        hook_lines.append(f"{i}. [{hook_type}] {hook_text}")
    
    return '\n'.join(hook_lines)


def format_company_context_for_prompt(context):
    """Format company context for prompt"""
    if not context or not context.get('company_context'):
        return ""
    
    lines = [f"\nCOMPANY CONTEXT:\n{context['company_context']}"]
    
    if context.get('reusable_hooks'):
        lines.append(f"Company uses: {', '.join(context['reusable_hooks'][:3])}")
    
    return '\n'.join(lines)
