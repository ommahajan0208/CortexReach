"""
Twitter/X Scraper - Extract data from Twitter/X profile
Note: Twitter API requires authentication. This is a basic implementation.
"""

import requests
from bs4 import BeautifulSoup


def scrape_x_profile(x_url):
    """
    Scrape Twitter/X profile data
    
    Args:
        x_url: str - Twitter/X profile URL
    
    Returns:
        dict: {
            'username': str,
            'bio': str,
            'recent_tweets': list,
            'interests': list
        }
    """
    print(f"\n[INPUT] Scraping Twitter/X profile...")
    
    result = {
        'username': None,
        'bio': None,
        'recent_tweets': [],
        'interests': []
    }
    
    try:
        # Twitter/X has strong anti-scraping measures
        # For production, you'd want to:
        # 1. Use Twitter API v2 (requires authentication)
        # 2. Use a scraping service like Apify
        # 3. Use browser automation
        
        # For now, collect manually
        print("\nTwitter/X scraping requires authentication.")
        print("Please provide the information manually:\n")
        
        result['username'] = extract_x_username(x_url)
        print(f"Username: @{result['username']}")
        
        result['bio'] = input("Bio (optional): ").strip() or None
        
        recent_input = input("Recent tweet/thought (optional): ").strip()
        if recent_input:
            result['recent_tweets'] = [recent_input]
        
        interests_input = input("Interests/topics they tweet about (comma-separated, optional): ").strip()
        if interests_input:
            result['interests'] = [i.strip() for i in interests_input.split(',')]
        
        print("Twitter/X data collected")
        
    except Exception as e:
        print(f"Error collecting Twitter/X data: {str(e)}")
        return None
    
    return result


def extract_x_username(url):
    """Extract username from Twitter/X URL"""
    # twitter.com/username or x.com/username
    url = url.replace('twitter.com', 'x.com')
    if 'x.com/' in url:
        parts = url.split('x.com/')
        if len(parts) > 1:
            username = parts[1].split('/')[0].split('?')[0].replace('@', '')
            return username
    return None
