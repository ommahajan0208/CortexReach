"""
Ethics Validator - Check for manipulative or inappropriate content
"""

import re


def validate_ethics(content):
    """
    Check content for ethical concerns
    
    Args:
        content: str - generated content
    
    Returns:
        dict: {
            'is_valid': bool,
            'concerns': list of str,
            'suggestion': str
        }
    """
    concerns = []
    content_lower = content.lower()
    
    # Check for manipulative language
    manipulative_phrases = [
        'limited time offer',
        'act now',
        'don\'t miss out',
        'once in a lifetime',
        'exclusive deal',
        'guaranteed',
        'risk-free',
        'no obligation',
        'free money',
        'get rich'
    ]
    
    for phrase in manipulative_phrases:
        if phrase in content_lower:
            concerns.append(f"Contains potentially manipulative phrase: '{phrase}'")
    
    # Check for urgency/pressure tactics
    urgency_words = ['urgent', 'immediately', 'hurry', 'expires', 'deadline']
    urgency_count = sum(1 for word in urgency_words if word in content_lower)
    
    if urgency_count > 2:
        concerns.append("Excessive urgency/pressure language detected")
    
    # Check for overpromising
    overpromise_words = ['guarantee', 'promise', 'definitely', '100%', 'always']
    overpromise_count = sum(1 for word in overpromise_words if word in content_lower)
    
    if overpromise_count > 1:
        concerns.append("May be overpromising results")
    
    # Check for excessive capitalization (shouting)
    caps_ratio = sum(1 for c in content if c.isupper()) / max(len(content), 1)
    if caps_ratio > 0.3:
        concerns.append("Excessive capitalization detected")
    
    # Check length for spam-like characteristics
    if len(content) < 50:
        concerns.append("Content too short, may appear spammy")
    
    is_valid = len(concerns) == 0
    suggestion = ""
    
    if not is_valid:
        suggestion = "Consider revising to be more genuine and less pushy"
    
    return {
        'is_valid': is_valid,
        'concerns': concerns,
        'suggestion': suggestion
    }


def validate_ethics_and_display(content):
    """
    Validate ethics and display results
    
    Args:
        content: str
    
    Returns:
        bool: True if valid, False otherwise
    """
    print("\n[VALIDATION] Checking ethics...")
    
    result = validate_ethics(content)
    
    if result['is_valid']:
        print("Ethics check passed")
        return True
    else:
        print("Ethical concerns found:")
        for concern in result['concerns']:
            print(f"   - {concern}")
        if result['suggestion']:
            print(f"\nSuggestion: {result['suggestion']}")
        return False
