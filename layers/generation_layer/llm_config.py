"""
LLM Configuration - Configure offline LLM settings
"""

import requests


def get_llm_config():
    """
    Get LLM configuration from user
    
    Returns:
        dict: {
            'model_name': str,
            'api_url': str,
            'language': str,
            'temperature': float,
            'provider': str
        }
    """
    print("LLM CONFIGURATION")
    
    # Default config
    config = {
        'model_name': 'llama3',
        'api_url': 'http://localhost:11434',
        'language': 'English',
        'temperature': 0.8,
        'provider': 'ollama'
    }
    
    # Check if Ollama is running
    print("\nChecking for Ollama...")
    
    if is_ollama_available(config['api_url']):
        print("Ollama is running")
        
        # Ask for model
        print("\nDefault model: llama3")

        print("\nRecommended models:")
        print("   - llama2 (fast)")
        print("   - mistral (better quality)")
        print("   - llama3 (default, best quality)")

        model_input = input("Enter model name (or press Enter for default): ").strip()
        if model_input:
            config['model_name'] = model_input
        
    else:
        print("Ollama is not running!")
        print("\nPlease start Ollama:")
        print("   1. Install from: https://ollama.ai")
        print("   2. Run: ollama pull llama2")
        print("   3. Start Ollama service")
        print("\nRecommended models:")
        print("   - llama2 (default, fast)")
        print("   - mistral (better quality)")
        print("   - llama3 (best quality, slower)")
        
        input("\nPress Enter after starting Ollama...")
        
        if not is_ollama_available(config['api_url']):
            print("\nStill cannot connect to Ollama. Exiting.")
            return None
        
        print("Ollama connected!")
    
    return config


def is_ollama_available(api_url):
    """Check if Ollama is available"""
    try:
        response = requests.get(f"{api_url}/api/tags", timeout=2)
        return response.status_code == 200
    except:
        return False


def list_available_models(api_url):
    """List available Ollama models"""
    try:
        response = requests.get(f"{api_url}/api/tags", timeout=2)
        if response.status_code == 200:
            data = response.json()
            models = [m['name'] for m in data.get('models', [])]
            return models
    except:
        pass
    return []
