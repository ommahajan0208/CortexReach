"""
Company Matcher - Find previous prospects from the same company
"""

import json
import os


def find_same_company_prospects(company_name, client_id, data_dir='data'):
    """
    Find prospects from the same company in past outreach
    
    Args:
        company_name: str - company to match
        client_id: str - client ID
        data_dir: str - data directory path
    
    Returns:
        list of dict: previous prospects from same company
    """
    print(f"\n[CONTEXT] Checking for prospects from {company_name}...")
    
    if not company_name:
        print("No company name provided, skipping company matching")
        return []
    
    prospects_file = os.path.join(data_dir, client_id, 'prospects.json')
    
    if not os.path.exists(prospects_file):
        print("No previous prospects found (first time)")
        return []
    
    try:
        with open(prospects_file, 'r', encoding='utf-8') as f:
            all_prospects = json.load(f)
        
        # Find prospects from same company (case-insensitive)
        company_lower = company_name.lower()
        same_company = [
            p for p in all_prospects 
            if p.get('company', '').lower() == company_lower
        ]
        
        if same_company:
            print(f"Found {len(same_company)} previous prospect(s) from {company_name}")
        else:
            print(f"No previous prospects from {company_name}")
        
        return same_company
        
    except Exception as e:
        print(f"Error loading prospects: {str(e)}")
        return []
