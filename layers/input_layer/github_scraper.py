"""
GitHub Scraper - Extract data from GitHub profile
Uses GitHub's public API (no authentication needed for public profiles)
"""

import requests
import time


def scrape_github_profile(github_url):
    """
    Scrape GitHub profile data using GitHub API
    
    Args:
        github_url: str - GitHub profile URL
    
    Returns:
        dict: {
            'username': str,
            'projects': list,
            'languages': list,
            'contribution_activity': str
        }
    """
    print(f"\n[INPUT] Scraping GitHub profile...")
    
    result = {
        'username': None,
        'projects': [],
        'languages': [],
        'contribution_activity': None
    }
    
    try:
        username = extract_github_username(github_url)
        if not username:
            print("Invalid GitHub URL")
            return None
        
        result['username'] = username
        
        # GitHub API endpoint
        api_base = 'https://api.github.com'
        headers = {'Accept': 'application/vnd.github.v3+json'}
        
        # Get user info
        user_response = requests.get(
            f'{api_base}/users/{username}',
            headers=headers,
            timeout=10
        )
        
        if user_response.status_code != 200:
            print(f"GitHub user not found: {username}")
            return None
        
        user_data = user_response.json()
        
        # Get repositories
        repos_response = requests.get(
            f'{api_base}/users/{username}/repos?sort=updated&per_page=10',
            headers=headers,
            timeout=10
        )
        
        if repos_response.status_code == 200:
            repos = repos_response.json()
            
            # Extract project names and languages
            languages_set = set()
            projects = []
            
            for repo in repos[:5]:  # Top 5 recent repos
                if not repo.get('fork'):  # Skip forked repos
                    projects.append({
                        'name': repo['name'],
                        'description': repo.get('description', ''),
                        'stars': repo.get('stargazers_count', 0)
                    })
                    
                    if repo.get('language'):
                        languages_set.add(repo['language'])
            
            result['projects'] = projects
            result['languages'] = list(languages_set)
        
        # Contribution activity summary
        public_repos = user_data.get('public_repos', 0)
        if public_repos > 0:
            result['contribution_activity'] = f"{public_repos} public repositories"
        
        print(f"GitHub data collected: @{username}")
        print(f"   Projects: {len(result['projects'])}")
        print(f"   Languages: {', '.join(result['languages'][:3])}")
        
    except requests.RequestException as e:
        print(f"Error scraping GitHub: {str(e)}")
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None
    
    return result


def extract_github_username(url):
    """Extract username from GitHub URL"""
    # github.com/username
    if 'github.com/' in url:
        parts = url.split('github.com/')
        if len(parts) > 1:
            username = parts[1].split('/')[0].split('?')[0]
            return username
    return None
