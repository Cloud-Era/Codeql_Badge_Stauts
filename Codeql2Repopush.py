from github import Github

# GitHub personal access token
access_token = 'gh_em25Mu426fjNdRyXWXpy4ae¡PhMX®Dmv@Q*'
# Create a GitHub instance
g = Github(access_token)

# Organization name
org_name = 'new-gen-omega'

def create_pr(repo, title, body, changes):
    try:
        pr = repo.create_pull(title=title, body=body, head="main", base="main")
        print(f"Pull request created for repository: {repo.full_name}")
        for filename, content in changes.items():
            pr.create_file(filename, f"Add {filename}", content, branch="main")
        print(f"Changes added to pull request for repository: {repo.full_name}")
    except Exception as e:
        print(f"Error creating pull request for repository {repo.full_name}: {e}")

if __name__ == "__main__":
    try:
        org = g.get_organization(org_name)
        print(f"Fetching repositories for organization: {org_name}")

        # List of repository names
        repo_names = ["repo1", "repo2", "repo3", "repo4", "repo5"]

        for repo_name in repo_names:
            repo = org.get_repo(repo_name)
            
            # Title and body of the pull request
            pr_title = "Add CodeQL badge and documentation"
            pr_body = "This pull request adds a CodeQL badge to the README file and includes documentation."
            
            # Changes to be made in the pull request (README file)
            changes = {
                "README.md": "# README\n\n[![CodeQL](https://github.com/your-username/your-repository/workflows/CodeQL/badge.svg)](https://github.com/your-username/your-repository/actions)\n\nAdd your documentation here."
            }

            # Create pull request
            create_pr(repo, pr_title, pr_body, changes)
    except Exception as e:
        print(f"Error fetching repositories: {e}")
