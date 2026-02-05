"""
Website Scraper - Extract company information from website
"""

import requests
from bs4 import BeautifulSoup
import re


def scrape_company_website(website_url):
    """
    Scrape company website for information
    
    Args:
        website_url: str - Company website URL
    
    Returns:
        dict: {
            'company_name': str,
            'description': str,
            'tech_stack': list,
            'industry': str
        }
    """
    print(f"\n[INPUT] Scraping company website...")
    
    result = {
        'company_name': None,
        'description': None,
        'tech_stack': [],
        'industry': None
    }
    
    try:
        # Add headers to mimic browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # Fetch the page
        response = requests.get(website_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Try to extract company name
        # Look in title, h1, og:site_name meta tag
        title_tag = soup.find('title')
        if title_tag:
            result['company_name'] = title_tag.text.strip().split('|')[0].strip()
        
        og_site = soup.find('meta', property='og:site_name')
        if og_site and og_site.get('content'):
            result['company_name'] = og_site['content'].strip()
        
        # Try to extract description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            result['description'] = meta_desc['content'].strip()
        
        og_desc = soup.find('meta', property='og:description')
        if og_desc and og_desc.get('content') and not result['description']:
            result['description'] = og_desc['content'].strip()
        
        # Try to detect tech stack from scripts, meta tags
        scripts = soup.find_all('script', src=True)
        tech_indicators = {
            'react': ['react', 'jsx'],
            'vue': ['vue'],
            'angular': ['angular'],
            'next.js': ['next'],
            'wordpress': ['wp-content', 'wordpress'],
            'shopify': ['shopify'],
            'google analytics': ['google-analytics', 'gtag'],
            'stripe': ['stripe']
        }
        
        detected_tech = set()
        page_text = str(soup).lower()
        
        for tech, indicators in tech_indicators.items():
            if any(ind in page_text for ind in indicators):
                detected_tech.add(tech)
        
        result['tech_stack'] = list(detected_tech)
        
        # Try to infer industry from content (basic keyword matching)
        content = soup.get_text().lower()
        industry_keywords = {
            'saas': ['software', 'saas', 'cloud', 'platform'],
            'ecommerce': ['shop', 'store', 'ecommerce', 'buy', 'cart'],
            'fintech': ['fintech', 'financial', 'payment', 'banking'],
            'healthcare': ['health', 'medical', 'patient', 'clinic'],
            'education': ['education', 'learning', 'course', 'student'],
            'marketing': ['marketing', 'advertising', 'campaign'],
        }
        
        for industry, keywords in industry_keywords.items():
            if sum(content.count(kw) for kw in keywords) > 3:
                result['industry'] = industry
                break
        
        print(f"Website scraped: {result['company_name'] or 'Unknown company'}")
        
    except requests.RequestException as e:
        print(f"Error scraping website: {str(e)}")
        print("Continuing without website data...")
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None
    
    return result
