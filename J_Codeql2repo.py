import os
import json
import requests
from git import Repo, Actor

def create_workflow_status_badge_pr(repo_owner, repo_name, access_token):
    # Construct the URL for the GitHub API endpoint to create a PR
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
    
    # Prepare the PR body
    pr_body = {
        "title": "Add workflow status badge",
        "body": "This PR adds a workflow status badge to the README file.",
        "head": "add-workflow-status-badge",
        "base": "main"
    }
    
    # Add the workflow status badge markdown to the PR body
    pr_body["body"] += "\n\n### Workflows\n\n![Workflow Status](https://img.shields.io/github/workflow/status/{}/{}/CI)".format(repo_owner, repo_name)

    # Prepare the request headers with authentication token
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Send POST request to create the PR
    response = requests.post(url, headers=headers, data=json.dumps(pr_body))

    # Check if PR creation was successful
    if response.status_code == 201:
        print(f"Pull request created successfully for {repo_owner}/{repo_name}")
    else:
        print(f"Failed to create pull request for {repo_owner}/{repo_name}")
        print(f"Response: {response.text}")

def main():
    # GitHub access token
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")

    # Repositories to add workflow status badge
    repositories = [
        {"owner": "owner1", "name": "repo1"},
        {"owner": "owner2", "name": "repo2"}
    ]

    # Iterate over repositories and create PR for each
    for repo in repositories:
        create_workflow_status_badge_pr(repo["owner"], repo["name"], access_token)

if __name__ == "__main__":
    main()
