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
        
        # Parse hooks (simple implementation)
        hooks = parse_hooks_from_text(hooks_text, prospect_data)
        
        # Import rich display
        try:
            from layers.visualization_layer.console_manager import print_hooks_table
            print_hooks_table(hooks)
        except ImportError:
            # Fallback to simple display
            print(f"Extracted {len(hooks)} personalization hooks")
            if hooks:
                print("\n[HOOKS] Personalization hooks extracted:")
                for i, hook in enumerate(hooks, 1):
                    hook_text = hook['hook_text']
                    hook_type = hook.get('hook_type', 'general')
                    display_text = hook_text if len(hook_text) <= 80 else hook_text[:77] + "..."
                    print(f"  {i}. [{hook_type}] {display_text}")
        
        return hooks
        
    except Exception as e:
        print(f"Error extracting hooks: {str(e)}")
        # Fallback to rule-based hooks
        hooks = extract_basic_hooks(prospect_data)
        
        # Display fallback hooks
        try:
            from layers.visualization_layer.console_manager import print_hooks_table
            print_hooks_table(hooks)
        except ImportError:
            # Fallback display
            if hooks:
                print(f"Using {len(hooks)} rule-based hooks (fallback)")
                print("\n[HOOKS] Personalization hooks extracted:")
                for i, hook in enumerate(hooks, 1):
                    hook_text = hook['hook_text']
                    hook_type = hook.get('hook_type', 'general')
                    display_text = hook_text if len(hook_text) <= 80 else hook_text[:77] + "..."
                    print(f"  {i}. [{hook_type}] {display_text}")
        
        return hooks


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


def parse_hooks_from_text(text, prospect_data):
    """Parse hooks from LLM output"""
    hooks = []
    
    # Split by lines and look for hook patterns
    lines = text.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if line and len(line) > 10:
            # Remove bullet points, numbers
            cleaned = line.lstrip('- •*0123456789. ')
            if cleaned:
                hooks.append({
                    'hook_type': 'llm_generated',
                    'hook_text': cleaned,
                    'relevance_score': 0.8
                })
    
    # If no hooks parsed, fall back
    if not hooks:
        hooks = extract_basic_hooks(prospect_data)
    
    return hooks[:5]  # Top 5 hooks


def extract_basic_hooks(prospect_data):
    """Rule-based hook extraction as fallback"""
    hooks = []
    
    if prospect_data.get('recent_activity'):
        hooks.append({
            'hook_type': 'recent_activity',
            'hook_text': prospect_data['recent_activity'][0][:150],
            'relevance_score': 0.9
        })
    
    if prospect_data.get('projects') and len(prospect_data['projects']) > 0:
        proj = prospect_data['projects'][0]
        hooks.append({
            'hook_type': 'project',
            'hook_text': f"Working on {proj['name']} - {proj.get('description', '')}",
            'relevance_score': 0.8
        })
    
    if prospect_data.get('tech_stack'):
        hooks.append({
            'hook_type': 'tech_stack',
            'hook_text': f"Using {', '.join(prospect_data['tech_stack'][:3])}",
            'relevance_score': 0.7
        })
    
    if prospect_data.get('role') and prospect_data.get('company'):
        hooks.append({
            'hook_type': 'role',
            'hook_text': f"{prospect_data['role']} at {prospect_data['company']}",
            'relevance_score': 0.9
        })
    
    return hooks[:5]
