"""
Reference Builder - Build natural references to past outreach
"""


def build_company_reference(same_company_prospects):
    """
    Build a natural reference to previous outreach at the same company
    
    Args:
        same_company_prospects: list - prospects from same company
    
    Returns:
        str: natural reference text or None
    """
    print("\n[CONTEXT] Building company reference...")
    
    if not same_company_prospects or len(same_company_prospects) == 0:
        print("No reference needed (first contact at company)")
        return None
    
    # Build reference based on previous prospects
    num_previous = len(same_company_prospects)
    
    if num_previous == 1:
        prev = same_company_prospects[0]
        name = prev.get('name', 'someone')
        role = prev.get('role', 'your team')
        
        reference = f"We recently connected with {name} from {role}"
        
    else:
        # Multiple previous contacts
        reference = f"We've been connecting with members of your team"
    
    print(f"Built reference: {reference[:50]}...")
    
    return reference


def format_reference_for_prompt(reference):
    """
    Format reference for inclusion in generation prompt
    
    Args:
        reference: str or None
    
    Returns:
        str: formatted reference text for prompt
    """
    if not reference:
        return ""
    
    return f"\nOPTIONAL REFERENCE (use naturally if it fits):\n{reference}\n"
