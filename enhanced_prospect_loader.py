"""
Enhanced Prospect Loader - Supports both fake data and live scraping
Integrates fake_data_loader for comprehensive testing
"""

from layers.input_layer.prospect_loader import (
    display_input_menu, 
    display_channel_menu, 
    merge_prospect_data
)
from fake_data_loader import (
    display_prospect_menu,
    get_fake_prospect,
    get_fake_prospect_with_sources,
    FAKE_PROSPECTS
)


def get_data_mode():
    """
    Ask user whether to use fake data or scrape live data
    
    Returns:
        str: 'fake' or 'live' or None
    """
    print("\n" + "="*70)
    print("DATA SOURCE MODE")
    print("="*70)
    print("\nChoose how you want to provide prospect data:")
    print("  1. Use Fake Data (comprehensive test data covering all features)")
    print("  2. Scrape Live Data (real-time data from LinkedIn, websites, etc.)")
    print("\nNote: Fake data is pre-loaded and instant. Live data requires URLs.")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    if choice == '1':
        return 'fake'
    elif choice == '2':
        return 'live'
    else:
        print("Invalid choice. Please select 1 or 2.")
        return None


def get_fake_data_inputs():
    """
    Get inputs when using fake data mode
    
    Returns:
        dict: {
            'mode': 'fake',
            'prospect_id': str,
            'prospect_data': dict,
            'linkedin_data': dict,
            'website_data': dict,
            'x_data': dict,
            'github_data': dict,
            'selected_channels': list
        }
    """
    print("\n" + "="*70)
    print("FAKE DATA MODE")
    print("="*70)
    
    # Display prospect menu
    display_prospect_menu()
    
    # Get prospect selection
    print("\nEnter prospect ID (e.g., 'tech_001') or 'random' for random:")
    prospect_id = input("> ").strip().lower()
    
    if prospect_id == 'random':
        import random
        prospect_id = random.choice(list(FAKE_PROSPECTS.keys()))
        print(f"\nRandomly selected: [{prospect_id}] {FAKE_PROSPECTS[prospect_id]['name']}")
    
    if prospect_id not in FAKE_PROSPECTS:
        print(f"\nInvalid prospect ID: {prospect_id}")
        return None
    
    # Get the prospect data
    prospect_data = get_fake_prospect(prospect_id)
    linkedin_data, website_data, x_data, github_data = get_fake_prospect_with_sources(prospect_id)
    
    # Show what data is available
    print("\n" + "="*70)
    print(f"SELECTED: {prospect_data['name']}")
    print("="*70)
    print(f"Role: {prospect_data['role']}")
    print(f"Company: {prospect_data['company']}")
    print(f"Industry: {prospect_data['industry']}")
    
    print("\nAvailable data sources:")
    print(f"  ✓ LinkedIn: {prospect_data['name']}")
    print(f"  ✓ Website: {prospect_data['company']}")
    print(f"  ✓ Twitter/X: {len(prospect_data['recent_activity'])} recent activities")
    if github_data:
        print(f"  ✓ GitHub: {len(prospect_data['projects'])} projects")
    else:
        print(f"  ✗ GitHub: Not available for this prospect")
    
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
    selected_channels = [
        channel_map[num] for num in selected_channel_nums 
        if num in channel_map
    ]
    
    if not selected_channels:
        print("No valid channels selected. Exiting.")
        return None
    
    print(f"\nChannels selected: {', '.join(selected_channels)}")
    
    return {
        'mode': 'fake',
        'prospect_id': prospect_id,
        'prospect_data': prospect_data,
        'linkedin_data': linkedin_data,
        'website_data': website_data,
        'x_data': x_data,
        'github_data': github_data,
        'selected_channels': selected_channels,
        # For compatibility with live mode
        'linkedin_url': None,
        'website_url': None,
        'x_url': None,
        'github_url': None
    }


def get_live_data_inputs():
    """
    Get inputs when using live scraping mode
    
    Returns:
        dict: {
            'mode': 'live',
            'linkedin_url': str or None,
            'website_url': str or None,
            'x_url': str or None,
            'github_url': str or None,
            'selected_channels': list
        }
    """
    print("\n" + "="*70)
    print("LIVE SCRAPING MODE")
    print("="*70)
    
    result = {
        'mode': 'live',
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
    
    print("\nENTER URLs")
    
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


def get_enhanced_user_inputs():
    """
    Enhanced input collection that supports both fake and live data
    
    Returns:
        dict: Contains mode, data sources, and selected channels
    """
    # Ask for data mode
    mode = get_data_mode()
    
    if not mode:
        return None
    
    if mode == 'fake':
        return get_fake_data_inputs()
    else:
        return get_live_data_inputs()


# For testing
if __name__ == "__main__":
    print("Enhanced Prospect Loader - Testing")
    print("-" * 70)
    
    inputs = get_enhanced_user_inputs()
    
    if inputs:
        print("\n" + "="*70)
        print("RESULT:")
        print("="*70)
        print(f"Mode: {inputs['mode']}")
        print(f"Channels: {inputs['selected_channels']}")
        
        if inputs['mode'] == 'fake':
            print(f"\nProspect: {inputs['prospect_data']['name']}")
            print(f"Company: {inputs['prospect_data']['company']}")
            print(f"Skills: {', '.join(inputs['prospect_data']['skills'][:5])}")
        else:
            print(f"\nLinkedIn URL: {inputs['linkedin_url']}")
            print(f"Website URL: {inputs['website_url']}")
            print(f"GitHub URL: {inputs['github_url']}")
