"""
Persona Analyzer - Analyze prospect's persona using LLM
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from config.prompts import PERSONA_ANALYSIS_PROMPT, PERSONA_TYPE_PROMPT, KEY_INTERESTS_PROMPT


def analyze_persona(prospect_data, llm_generate_func, llm_config):
    """
    Analyze prospect's persona and communication style
    
    Args:
        prospect_data: dict - merged prospect data
        llm_generate_func: function - LLM generation function
        llm_config: dict - LLM configuration
    
    Returns:
        dict: {
            'persona_type': str,
            'communication_style': str,
            'key_interests': list
        }
    """
    print("\n[ANALYSIS] Analyzing prospect persona...")
    
    # Format prospect data for prompt
    data_summary = format_prospect_data(prospect_data)
    
    
    
    try:
        # Generate communication style analysis
        style_prompt = PERSONA_ANALYSIS_PROMPT.format(prospect_data=data_summary)
        communication_style = llm_generate_func(style_prompt, llm_config).strip().lower()
        
        # Validate the returned style
        valid_styles = [
            "executive",     # short, high-value, decision-focused
            "technical",     # logical, detailed, data-driven
            "friendly",      # warm, personalized, human
            "formal",        # professional, structured, low slang
            "skeptical"      # low-pressure, trust-building
        ]
        if communication_style not in valid_styles:
            communication_style = 'formal'  # Default fallback
        
        # Generate persona type analysis
        type_prompt = PERSONA_TYPE_PROMPT.format(prospect_data=data_summary)
        persona_type = llm_generate_func(type_prompt, llm_config).strip().lower()
        
        # Validate the returned persona type
        valid_types = [
            "innovator",      # early adopters, tech enthusiasts
            "builder",        # makers, creators, developers
            "analyst",        # data-driven, researchers
            "leader",         # managers, executives
            "specialist",     # deep experts
            "entrepreneur"    # founders, business builders
        ]
        if persona_type not in valid_types:
            persona_type = 'builder'  # Default fallback
        
        # Generate key interests analysis
        interests_prompt = KEY_INTERESTS_PROMPT.format(prospect_data=data_summary)
        interests_result = llm_generate_func(interests_prompt, llm_config).strip()
        
        # Parse comma-separated interests
        key_interests = [i.strip() for i in interests_result.split(',') if i.strip()]
        if not key_interests:
            key_interests = prospect_data.get('interests', [])[:3]  # Fallback
        
        result = {
            'persona_type': persona_type,
            'communication_style': communication_style,
            'key_interests': key_interests
        }
        
        print(f"Persona analyzed: {result['persona_type']} | {result['communication_style']} communicator")
        
        return result
        
    except Exception as e:
        print(f"Error analyzing persona: {str(e)}")
        # Return basic analysis
        return {
            'persona_type': 'builder',
            'communication_style': 'formal',
            'key_interests': []
        }

def format_prospect_data(data):
    """Format prospect data for LLM prompt"""
    lines = []
    
    if data.get('name'):
        lines.append(f"Name: {data['name']}")
    if data.get('role'):
        lines.append(f"Role: {data['role']}")
    if data.get('company'):
        lines.append(f"Company: {data['company']}")
    if data.get('bio'):
        lines.append(f"Bio: {data['bio']}")
    if data.get('skills'):
        lines.append(f"Skills: {', '.join(data['skills'][:5])}")
    if data.get('tech_stack'):
        lines.append(f"Tech Stack: {', '.join(data['tech_stack'][:5])}")
    if data.get('interests'):
        lines.append(f"Interests: {', '.join(data['interests'][:5])}")
    if data.get('recent_activity'):
        lines.append(f"Recent Activity: {data['recent_activity'][0][:200]}")
    if data.get('projects'):
        proj_names = [p['name'] for p in data['projects'][:3]]
        lines.append(f"Projects: {', '.join(proj_names)}")
    
    return '\n'.join(lines) if lines else "Limited data available"
