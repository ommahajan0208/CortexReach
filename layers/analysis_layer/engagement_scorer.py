"""
Engagement Scorer - Predict likelihood of engagement
"""


def calculate_engagement_score(prospect_data, persona_data):
    """
    Calculate engagement score (0-100) based on data quality and signals
    
    Args:
        prospect_data: dict - merged prospect data
        persona_data: dict - persona analysis
    
    Returns:
        float: engagement score (0-100)
    """
    print("\n[ANALYSIS] Calculating engagement score...")
    
    score = 30.0  # Base score
    
    # Data completeness (more data = better personalization = higher engagement)
    if prospect_data.get('name'):
        score += 5
    if prospect_data.get('role'):
        score += 5
    if prospect_data.get('company'):
        score += 5
    if prospect_data.get('bio'):
        score += 5
    
    # Activity signals
    if prospect_data.get('recent_activity'):
        score += 10  # Active on social media
    
    if prospect_data.get('projects') and len(prospect_data['projects']) > 0:
        score += 5  # Active on GitHub
    
    # Interest/skill data
    if prospect_data.get('skills') and len(prospect_data['skills']) > 3:
        score += 5
    
    if prospect_data.get('interests') and len(prospect_data['interests']) > 2:
        score += 5
    
    # Tech stack knowledge
    if prospect_data.get('tech_stack') and len(prospect_data['tech_stack']) > 0:
        score += 5
    
    # Company context
    if prospect_data.get('company_description'):
        score += 5
    
    # Cap at 100
    score = min(score, 100.0)
    
    print(f"Engagement score: {score}/100")
    
    return score
