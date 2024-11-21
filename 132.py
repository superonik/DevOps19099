import requests

username = "avielb"
url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)
if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        if "devops" in str(repo["full_name"]).lower() :
            print(f"{name} - {repo["full_name"]}")


