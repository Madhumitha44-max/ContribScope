import  requests

def get_repository(owner , repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url,timeout=10)
    if response.status_code == 200:
        return response.json()
    print("Failed to fetch repository data")
    print("status_code :",response.status_code)
    return None
