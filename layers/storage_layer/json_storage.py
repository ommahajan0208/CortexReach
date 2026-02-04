"""
JSON Storage - Save and load data to/from JSON files
"""

import json
import os
from datetime import datetime


def save_prospect(prospect_data, generated_outputs, client_id, data_dir='data'):
    """
    Save prospect data and generated outputs
    
    Args:
        prospect_data: dict - prospect information
        generated_outputs: dict - generated content by channel
        client_id: str - client ID
        data_dir: str - data directory path
    
    Returns:
        str: filepath where data was saved
    """
    print("\n[STORAGE] Saving prospect data...")
    
    prospects_file = os.path.join(data_dir, client_id, 'prospects.json')
    
    # Load existing prospects
    try:
        with open(prospects_file, 'r', encoding='utf-8') as f:
            prospects = json.load(f)
    except:
        prospects = []
    
    # Create prospect record
    record = {
        'prospect_data': prospect_data,
        'generated_outputs': generated_outputs,
        'timestamp': datetime.now().isoformat(),
        'client_id': client_id
    }
    
    # Add to prospects
    prospects.append(record)
    
    # Save
    with open(prospects_file, 'w', encoding='utf-8') as f:
        json.dump(prospects, f, indent=2, ensure_ascii=False)
    
    print(f"Prospect data saved to {prospects_file}")
    
    return prospects_file


def load_prospects(client_id, data_dir='data'):
    """
    Load all prospects for a client
    
    Args:
        client_id: str
        data_dir: str
    
    Returns:
        list: all prospects
    """
    prospects_file = os.path.join(data_dir, client_id, 'prospects.json')
    
    if not os.path.exists(prospects_file):
        return []
    
    try:
        with open(prospects_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []


def save_session_log(log_data, client_id, data_dir='data'):
    """
    Save session log for debugging/tracking
    
    Args:
        log_data: dict
        client_id: str
        data_dir: str
    """
    log_file = os.path.join(
        data_dir, 
        client_id, 
        f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )
    
    try:
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Could not save session log: {str(e)}")
