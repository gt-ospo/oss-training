# Let's Check Your Open Source Project Sustainability!
# This script analyzes a GitHub repository for sustainability indicators.
# <--- Instructions: --->
# First, run this cell to define the functions needed for analysis.
# Then run the cell below to test it with a specific repository URL!

import requests
from urllib.parse import urlparse

GITHUB_API = "https://api.github.com"

def extract_repo_info(url):
    """Extract user and repo name from GitHub URL"""
    path = urlparse(url).path.strip("/").split("/")
    if len(path) >= 2:
        return path[0], path[1]
    raise ValueError("Invalid GitHub repository URL")

def fetch_github_repo_metadata(user, repo):
    """Fetch repository metadata from GitHub API"""
    repo_api = f"{GITHUB_API}/repos/{user}/{repo}"
    response = requests.get(repo_api)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch metadata: {response.status_code}")

def check_file_exists(user, repo, file_path):
    """Check if a specific file exists in the repository"""
    url = f"{GITHUB_API}/repos/{user}/{repo}/contents/{file_path}"
    r = requests.get(url)
    return r.status_code == 200

def analyze_repo(url):
    """Analyze a GitHub repository for sustainability indicators"""
    user, repo = extract_repo_info(url)
    metadata = fetch_github_repo_metadata(user, repo)
    
    indicators = {
        "Has License": check_file_exists(user, repo, "LICENSE"),
        "Has Readme": check_file_exists(user, repo, "README.md"),
        "Has Contributing Guide": check_file_exists(user, repo, "CONTRIBUTING.md"),
        "Has Code of Conduct": check_file_exists(user, repo, "CODE_OF_CONDUCT.md"),
        "Has GitHub Actions": check_file_exists(user, repo, ".github/workflows"),
        "Open Issues": metadata.get("open_issues_count", 0),
        "Forks": metadata.get("forks_count", 0),
        "Stars": metadata.get("stargazers_count", 0),
        "Archived": metadata.get("archived", False),
        "Last Updated": metadata.get("updated_at"),
        "Community Engagement": metadata.get("subscribers_count", 0)
    }

    return indicators

def test_analyze_repo(repo_url):
    """Test the analyze_repo function with a provided GitHub URL"""
    indicators = analyze_repo(repo_url)
    print("--- Sustainability Indicators ---")
    
    # Define which metrics are boolean vs numeric
    boolean_metrics = {
        "Has License", "Has Readme", "Has Contributing Guide", 
        "Has Code of Conduct", "Has GitHub Actions", "Archived"
    }
    
    for key, value in indicators.items():
        if key in boolean_metrics:
            # For boolean metrics, use standard boolean logic
            emoji = "✅" if value else "❌"
        elif key == "Archived":
            # Archived should be ❌ if True (archived is bad for active projects)
            emoji = "❌" if value else "✅"
        elif isinstance(value, (int, float)):
            # For numeric metrics, show actual value without emoji judgment
            emoji = "📊"
        else:
            # For other types (like dates), just show the value
            emoji = "📅"
        
        print(f"{emoji} {key}: {value}")

repo_url = "https://github.com/gt-ospo/oss-training"
test_analyze_repo(repo_url)