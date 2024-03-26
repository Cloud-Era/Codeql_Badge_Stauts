import os
import requests
import csv

# GitHub personal access token
access_token = os.getenv('GITHUB_TOKEN')

# GitHub organization name
org_name = 'your_organization_name'

def check_codeql_workflow_enabled(repo_name):
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(f'https://api.github.com/repos/{org_name}/{repo_name}/actions/workflows', headers=headers)
    workflows = response.json().get('workflows', [])
    for workflow in workflows:
        if workflow.get('name') == 'CodeQL':
            return "Yes"
    return "No"

if __name__ == "__main__":
    csv_filename = "codeql_enabled_repos.csv"
    headers = ['Repository', 'CodeQL Workflow Enabled']

    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)

        # Fetch repositories in the organization
        response = requests.get(f'https://api.github.com/orgs/{org_name}/repos', headers=headers)
        if response.status_code == 200:
            repositories = response.json()  # Convert response to JSON
            print(f"Found {len(repositories)} repositories in the organization {org_name}.")

            for repo in repositories:
                repo_name = repo['name']
                codeql_enabled = check_codeql_workflow_enabled(repo_name)
                writer.writerow([repo_name, codeql_enabled])

            print(f"CSV file '{csv_filename}' created with CodeQL enabled repositories.")
        else:
            print(f"Failed to fetch repositories in the organization {org_name}: {response.text}")
