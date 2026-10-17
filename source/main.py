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
    print("Repository:", data["name"])
    print("Description:", data["description"])
    print("Stars:", data["stargazers_count"])
    print("Forks:", data["forks_count"])
    print("Open Issues:", data["open_issues_count"])
    print("Language:", data["language"])


if __name__ == "__main__":
    main()