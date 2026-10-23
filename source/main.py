from github_client import get_repository

def main():
    owner = input("Enter the GitHub username :").strip()
    repo = input("Enter the name of the repository :").strip()

    if not owner or not repo:
        print("Username and repository name cannot be empty!!")
        return
    data = get_repository(owner , repo)

    if data is None:
        return
    print("\n -----Repository Information-----")
    print("Repository:", data.get("name","Not available"))
    print("Description:", data.get("description") or "NOt available")
    print("Stars:", data.get("stargazers_count", "Not available"))
    print("Forks:", data.get("forks_count","Not available"))
    print("Open Issues:", data.get("open_issues_count" , "NOt available"))
    print("Language:", data.get("language") or "NOt available")


if __name__ == "__main__":
    main()