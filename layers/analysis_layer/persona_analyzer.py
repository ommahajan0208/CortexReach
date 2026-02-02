"""
Persona Analyzer - Analyze prospect's persona using LLM
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from config.prompts import PERSONA_ANALYSIS_PROMPT


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
            'key_interests': list,
            'pain_points': list
        }
    """
    print("\n[ANALYSIS] Analyzing prospect persona...")
    
    # Format prospect data for prompt
    data_summary = format_prospect_data(prospect_data)
    
    # Generate persona analysis
    prompt = PERSONA_ANALYSIS_PROMPT.format(prospect_data=data_summary)
    
    try:
        analysis_text = llm_generate_func(prompt, llm_config)
        
        # Parse the analysis (basic parsing)
        result = {
            'persona_type': 'professional',  # Default
            'communication_style': 'formal',
            'key_interests': prospect_data.get('interests', [])[:3],
            'pain_points': [],
            'raw_analysis': analysis_text
        }
        
        # Extract communication style from analysis
        analysis_lower = analysis_text.lower()
        if 'casual' in analysis_lower or 'informal' in analysis_lower:
            result['communication_style'] = 'casual'
        elif 'technical' in analysis_lower:
            result['communication_style'] = 'technical'
        
        print(f"Persona analyzed: {result['communication_style']} communicator")
        
        return result
        
    except Exception as e:
        print(f"Error analyzing persona: {str(e)}")
        # Return basic analysis
        return {
            'persona_type': 'professional',
            'communication_style': 'formal',
            'key_interests': prospect_data.get('interests', [])[:3],
            'pain_points': [],
            'raw_analysis': ''
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
