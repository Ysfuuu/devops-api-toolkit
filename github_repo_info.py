import requests
import argparse

def get_repo_info(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    content_type = response.headers.get("Content-Type", "")

    if "application/json" not in content_type:
        raise ValueError("Expected JSON but received: " + content_type)

    return response.json()

def display_repo_info(data):
    print("Name:", data["name"])
    print("Description:", data["description"])
    print("Private:", data["private"])
    print("Stars:", data["stargazers_count"])
    print("Default branch:", data["default_branch"])


def main():
    parser = argparse.ArgumentParser(description="Get GitHub repository information")

    parser.add_argument("owner", help="GitHub username or organization")
    parser.add_argument("repo", help="Repository name")

    args = parser.parse_args()

    try:
        data = get_repo_info(args.owner, args.repo)
        display_repo_info(data)

    except requests.exceptions.RequestException as error:
        print("API request failed:", error)

    except ValueError as error:
        print("Invalid API response:", error)