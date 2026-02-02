"""
Product/Service Configuration - CortexReach default information
Used internally for generating outreach content
"""

def get_default_product_info():
    """
    Get CortexReach product information (used silently)
    
    Returns:
        dict: Product details
    """
    return {
        'name': 'CortexReach',
        'tagline': 'AI-Powered Hyper-Personalized Outreach Engine',
        'description': 'An intelligent cold outreach automation platform that uses offline LLMs to generate highly personalized messages across multiple channels (Email, WhatsApp, SMS, LinkedIn, Instagram)',
        'key_features': [
            'Multi-source data collection (LinkedIn, Website, Twitter/X, GitHub)',
            'AI-powered persona analysis and engagement scoring',
            'Context-aware personalization using company insights',
            'Multi-channel message generation with privacy validation',
            'Client-based learning and continuous improvement'
        ],
        'value_propositions': [
            'Save 10+ hours per week on manual prospect research',
            'Increase response rates by 3-5x with hyper-personalization',
            'Scale outreach without sacrificing message quality',
            'Maintain privacy with offline LLM processing',
            'Learn from past interactions for better results'
        ],
        'target_audience': 'Sales professionals, founders, recruiters, marketers, and business development teams doing high-quality cold outreach at scale',
        'use_cases': [
            'B2B sales prospecting',
            'Talent recruiting',
            'Partnership outreach',
            'Investor relations',
            'Influencer collaboration'
        ]
    }


def format_product_for_prompt(product_info):
    """
    Format product information for LLM prompts
    
    Args:
        product_info: dict - product context
    
    Returns:
        str: formatted product information
    """
    lines = []
    
    lines.append(f"Product: {product_info['name']}")
    lines.append(f"What it does: {product_info['description']}")
    
    if product_info.get('value_propositions'):
        lines.append("\nCore Benefits:")
        for value in product_info['value_propositions'][:3]:
            lines.append(f"  • {value}")
    
    if product_info.get('target_audience'):
        lines.append(f"\nIdeal For: {product_info['target_audience']}")
    
    return '\n'.join(lines)
