"""
Hook Extractor - Extract personalization hooks from prospect data
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from config.prompts import HOOK_EXTRACTION_PROMPT


def extract_hooks(prospect_data, llm_generate_func, llm_config):
    """
    Extract personalization hooks from prospect data
    
    Args:
        prospect_data: dict - merged prospect data
        llm_generate_func: function - LLM generation function
        llm_config: dict - LLM configuration
    
    Returns:
        list of dict: [
            {
                'hook_type': str,
                'hook_text': str,
                'relevance_score': float
            }
        ]
    """
    print("\n[ANALYSIS] Extracting personalization hooks...")
    
    # Format prospect data
    data_summary = format_prospect_data_for_hooks(prospect_data)
    
    # Generate hooks using LLM
    prompt = HOOK_EXTRACTION_PROMPT.format(prospect_data=data_summary)
    
    try:
        hooks_text = llm_generate_func(prompt, llm_config)
        
        # Parse comma-separated hooks
        hooks = [h.strip() for h in hooks_text.strip().split(',') if h.strip()]
        
        # If no hooks parsed, return empty list
        if not hooks:
            return []
        
        hooks = hooks[:5]  # Top 5 hooks
        
        print(f"Extracted {len(hooks)} personalization hooks")
        
        return hooks
        
    except Exception as e:
        print(f"Error extracting hooks: {str(e)}")
        return []


def format_prospect_data_for_hooks(data):
    """Format prospect data emphasizing hook-worthy elements"""
    lines = []
    
    if data.get('name'):
        lines.append(f"Name: {data['name']}")
    if data.get('role'):
        lines.append(f"Role: {data['role']}")
    if data.get('company'):
        lines.append(f"Company: {data['company']}")
    
    if data.get('recent_activity'):
        lines.append(f"\nRecent Activity:")
        for activity in data['recent_activity'][:3]:
            lines.append(f"  - {activity}")
    
    if data.get('projects'):
        lines.append(f"\nProjects:")
        for proj in data['projects'][:3]:
            lines.append(f"  - {proj['name']}: {proj.get('description', 'N/A')}")
    
    if data.get('tech_stack'):
        lines.append(f"\nTech Stack: {', '.join(data['tech_stack'][:5])}")
    
    if data.get('skills'):
        lines.append(f"Skills: {', '.join(data['skills'][:5])}")
    
    if data.get('interests'):
        lines.append(f"Interests: {', '.join(data['interests'][:5])}")
    
    return '\n'.join(lines) if lines else "Limited data"
