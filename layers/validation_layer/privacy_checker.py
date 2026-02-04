"""
Privacy Checker - Ensure no sensitive data leaks in generated content
"""

import re


def check_privacy(content, prospect_data):
    """
    Check generated content for privacy violations
    
    Args:
        content: str - generated content
        prospect_data: dict - prospect data
    
    Returns:
        dict: {
            'is_valid': bool,
            'issues': list of str,
            'sanitized_content': str
        }
    """
    issues = []
    sanitized = content
    
    # Check for email addresses (shouldn't be in outreach message body)
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.search(email_pattern, content):
        issues.append("Contains email address in body")
    
    # Check for phone numbers
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    if re.search(phone_pattern, content):
        issues.append("Contains phone number")
    
    # Check for URLs that might expose private data
    private_url_patterns = [
        r'linkedin\.com/in/[^/\s]+/edit',  # LinkedIn edit URLs
        r'github\.com/[^/\s]+/settings',  # GitHub settings
    ]
    
    for pattern in private_url_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            issues.append("Contains private/settings URL")
    
    # Check for excessive personal data disclosure
    # (This is a basic check - could be enhanced with LLM-based analysis)
    
    is_valid = len(issues) == 0
    
    return {
        'is_valid': is_valid,
        'issues': issues,
        'sanitized_content': sanitized
    }


def validate_privacy(content, prospect_data):
    """
    Validate privacy and display results
    
    Args:
        content: str
        prospect_data: dict
    
    Returns:
        bool: True if valid, False otherwise
    """
    print("\n[VALIDATION] Checking privacy...")
    
    result = check_privacy(content, prospect_data)
    
    if result['is_valid']:
        print("Privacy check passed")
        return True
    else:
        print("Privacy issues found:")
        for issue in result['issues']:
            print(f"   - {issue}")
        return False
