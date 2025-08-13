from github_api.get_repos import GithubManager

manager = GithubManager()


def list_and_print_repos():
    print("Listing repositories:")
    repos, error = manager.list_github_data("REPOS")
    if error:
        print(f"Error fetching repositories: {error}")
        return

    if not repos:
        print("No repositories found.")

    for repo in repos:
        name = repo["name"]
        html_url = repo["html_url"]
        print(f"{name} - {html_url}")

def list_and_print_prs():
    print("\nListing pull requests:")
    prs_raw_data, error = manager.list_github_data("PRS")
    if error:
        print(f"Error fetching pull requests: {error}")
        return

    prs = prs_raw_data.get("items", [])
    if not prs:
        print("No pull requests found.")

    for pr in prs:
        title = pr["title"]
        html_url = pr["html_url"]
        print(f"{title} - {html_url}")


list_and_print_repos()
list_and_print_prs()