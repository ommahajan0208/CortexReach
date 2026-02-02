"""
Insight Reuser - Reuse insights from previous outreach to same company
"""

import json
import os


def reuse_company_insights(company_name, same_company_prospects, client_id, data_dir='data'):
    """
    Retrieve and reuse insights from previous outreach to same company
    
    Args:
        company_name: str - company name
        same_company_prospects: list - prospects from same company
        client_id: str - client ID
        data_dir: str - data directory path
    
    Returns:
        dict: {
            'reusable_hooks': list,
            'company_context': str,
            'proven_angles': list
        }
    """
    print(f"\n[CONTEXT] Reusing insights from previous {company_name} outreach...")
    
    result = {
        'reusable_hooks': [],
        'company_context': '',
        'proven_angles': []
    }
    
    if not same_company_prospects:
        print("No previous insights to reuse")
        return result
    
    # Load company insights cache
    insights_file = os.path.join(data_dir, client_id, 'company_insights.json')
    
    if os.path.exists(insights_file):
        try:
            with open(insights_file, 'r', encoding='utf-8') as f:
                company_insights = json.load(f)
            
            company_key = company_name.lower()
            if company_key in company_insights:
                cached = company_insights[company_key]
                result['company_context'] = cached.get('description', '')
                result['reusable_hooks'] = cached.get('hooks', [])
                result['proven_angles'] = cached.get('angles', [])
                
                print(f"Loaded {len(result['reusable_hooks'])} cached insights")
                return result
                
        except Exception as e:
            print(f"Error loading insights cache: {str(e)}")
    
    # Extract insights from previous prospects
    for prospect in same_company_prospects:
        # Extract company context
        if prospect.get('company_description') and not result['company_context']:
            result['company_context'] = prospect['company_description']
        
        # Extract tech stack as hooks
        if prospect.get('tech_stack'):
            for tech in prospect['tech_stack']:
                if tech not in result['reusable_hooks']:
                    result['reusable_hooks'].append(tech)
        
        # Extract industry
        if prospect.get('industry'):
            result['proven_angles'].append(f"Industry: {prospect['industry']}")
    
    print(f"Extracted insights from {len(same_company_prospects)} previous prospect(s)")
    
    return result


def save_company_insights(company_name, insights, prospect_data, client_id, data_dir='data'):
    """
    Save company insights for future reuse
    
    Args:
        company_name: str
        insights: dict - insights to save
        prospect_data: dict - current prospect data
        client_id: str
        data_dir: str
    """
    if not company_name:
        return
    
    insights_file = os.path.join(data_dir, client_id, 'company_insights.json')
    
    try:
        # Load existing insights
        if os.path.exists(insights_file):
            with open(insights_file, 'r', encoding='utf-8') as f:
                company_insights = json.load(f)
        else:
            company_insights = {}
        
        company_key = company_name.lower()
        
        # Update insights
        if company_key not in company_insights:
            company_insights[company_key] = {
                'description': prospect_data.get('company_description', ''),
                'industry': prospect_data.get('industry', ''),
                'hooks': list(set(insights.get('reusable_hooks', []))),
                'angles': list(set(insights.get('proven_angles', [])))
            }
        else:
            # Merge with existing
            existing = company_insights[company_key]
            if not existing.get('description') and prospect_data.get('company_description'):
                existing['description'] = prospect_data['company_description']
            
            # Merge hooks
            all_hooks = set(existing.get('hooks', [])) | set(insights.get('reusable_hooks', []))
            existing['hooks'] = list(all_hooks)
        
        # Save
        with open(insights_file, 'w', encoding='utf-8') as f:
            json.dump(company_insights, f, indent=2)
        
    except Exception as e:
        print(f"Error saving company insights: {str(e)}")
