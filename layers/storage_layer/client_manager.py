"""
Client Manager - Manage client IDs and client data
"""

import os
import json
import uuid
from datetime import datetime


def get_or_create_client_id(data_dir='data'):
    """
    Get existing client ID or create new one
    
    Args:
        data_dir: str - data directory path
    
    Returns:
        str: client_id
    """
    print("CLIENT IDENTIFICATION")
    
    # Ensure data directory exists
    os.makedirs(data_dir, exist_ok=True)
    
    # List existing clients
    existing_clients = []
    if os.path.exists(data_dir):
        existing_clients = [
            d for d in os.listdir(data_dir) 
            if os.path.isdir(os.path.join(data_dir, d))
        ]
    
    if existing_clients:
        print(f"\nFound {len(existing_clients)} existing client(s):")
        for i, client in enumerate(existing_clients, 1):
            print(f"  {i}. {client}")
        
        print(f"  {len(existing_clients) + 1}. Create new client")
        
        choice = input("\nSelect option: ").strip()
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(existing_clients):
                client_id = existing_clients[idx]
                print(f"\nUsing existing client: {client_id}")
                return client_id
        except:
            pass
    
    # Create new client
    client_id = f"client_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{str(uuid.uuid4())[:8]}"
    
    # Create client directory
    client_dir = os.path.join(data_dir, client_id)
    os.makedirs(client_dir, exist_ok=True)
    
    # Initialize empty files
    prospects_file = os.path.join(client_dir, 'prospects.json')
    insights_file = os.path.join(client_dir, 'company_insights.json')
    
    with open(prospects_file, 'w') as f:
        json.dump([], f)
    
    with open(insights_file, 'w') as f:
        json.dump({}, f)
    
    print(f"\nCreated new client: {client_id}")
    
    return client_id
