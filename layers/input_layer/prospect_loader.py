"""
Prospect Loader - Orchestrates input collection from user
Presents options and coordinates different input sources
"""


def display_input_menu():
    """Display input source options"""
    print("SELECT INPUT SOURCES")
    print("\nAvailable input sources (select multiple by comma-separating):")
    print("  1. LinkedIn URL")
    print("  2. Company Website URL")
    print("  3. Twitter/X URL")
    print("  4. GitHub URL")
    print("\nExample: 1,2,3 (for LinkedIn + Website + Twitter)")



def display_channel_menu():
    """Display output channel options"""
    print("\nSELECT OUTPUT CHANNELS")
    print("\nAvailable channels (select multiple by comma-separating):")
    print("  1. Email")
    print("  2. WhatsApp")
    print("  3. SMS")
    print("  4. LinkedIn DM")
    print("  5. Instagram DM")
    print("\nExample: 1,2,4 (for Email + WhatsApp + LinkedIn)")


def get_user_inputs():
    """
    Get input sources and channels from user
    
    Returns:
        dict: {
            'linkedin_url': str or None,
            'website_url': str or None,
            'x_url': str or None,
            'github_url': str or None,
            'selected_channels': list of str
        }
    """
    result = {
        'linkedin_url': None,
        'website_url': None,
        'x_url': None,
        'github_url': None,
        'selected_channels': []
    }
    
    # Get input sources
    display_input_menu()
    source_input = input("\nEnter source numbers (comma-separated): ").strip()
    
    if not source_input:
        print("No input sources selected. Exiting.")
        return None
    
    selected_sources = [s.strip() for s in source_input.split(',')]
    
    print("ENTER URLs")
    
    # Get URLs based on selection
    if '1' in selected_sources:
        result['linkedin_url'] = input("\nLinkedIn URL: ").strip() or None
    
    if '2' in selected_sources:
        result['website_url'] = input("Company Website URL: ").strip() or None
    
    if '3' in selected_sources:
        result['x_url'] = input("Twitter/X URL: ").strip() or None
    
    if '4' in selected_sources:
        result['github_url'] = input("GitHub URL: ").strip() or None
    
    # Get output channels
    display_channel_menu()
    channel_input = input("\nEnter channel numbers (comma-separated): ").strip()
    
    if not channel_input:
        print("No output channels selected. Exiting.")
        return None
    
    channel_map = {
        '1': 'email',
        '2': 'whatsapp',
        '3': 'sms',
        '4': 'linkedin',
        '5': 'instagram'
    }
    
    selected_channel_nums = [c.strip() for c in channel_input.split(',')]
    result['selected_channels'] = [
        channel_map[num] for num in selected_channel_nums 
        if num in channel_map
    ]
    
    if not result['selected_channels']:
        print("No valid channels selected. Exiting.")
        return None
    
    return result


def merge_prospect_data(linkedin_data, website_data, x_data, github_data):
    """
    Merge data from different sources into unified prospect data
    
    Args:
        linkedin_data: dict from linkedin_scraper
        website_data: dict from website_scraper
        x_data: dict from x_scraper
        github_data: dict from github_scraper
    
    Returns:
        dict: merged prospect data
    """
    merged = {
        'name': None,
        'role': None,
        'company': None,
        'bio': None,
        'skills': [],
        'recent_activity': [],
        'interests': [],
        'tech_stack': [],
        'projects': [],
        'industry': None,
        'company_description': None
    }
    
    # LinkedIn data (primary source for professional info)
    if linkedin_data:
        merged['name'] = linkedin_data.get('name')
        merged['role'] = linkedin_data.get('role')
        merged['company'] = linkedin_data.get('company')
        merged['bio'] = linkedin_data.get('bio')
        merged['skills'] = linkedin_data.get('skills', [])
        merged['recent_activity'].extend(linkedin_data.get('recent_posts', []))
    
    # Website data (company context)
    if website_data:
        if not merged['company']:
            merged['company'] = website_data.get('company_name')
        merged['company_description'] = website_data.get('description')
        merged['industry'] = website_data.get('industry')
        merged['tech_stack'].extend(website_data.get('tech_stack', []))
    
    # Twitter/X data (interests and recent thoughts)
    if x_data:
        merged['interests'].extend(x_data.get('interests', []))
        merged['recent_activity'].extend(x_data.get('recent_tweets', []))
    
    # GitHub data (technical profile)
    if github_data:
        merged['projects'] = github_data.get('projects', [])
        merged['tech_stack'].extend(github_data.get('languages', []))
        if github_data.get('contribution_activity'):
            merged['recent_activity'].append(
                f"Active on GitHub: {github_data['contribution_activity']}"
            )
    
    # Deduplicate lists
    merged['skills'] = list(set(merged['skills']))
    merged['tech_stack'] = list(set(merged['tech_stack']))
    merged['interests'] = list(set(merged['interests']))
    
    return merged
