import requests
from requests.auth import HTTPBasicAuth

base_url = 'https://api.github.com'
username = 'Saianshul1026'
token = 'your_token'  # Replace 'your_token' with your actual token

def get_user_info(base_url, username):
    headers = {'Authorization': f'token {token}'}
    response = requests.get(f'{base_url}/users/{username}', headers=headers, timeout=1)

    if response.status_code == 200:
        user_info = response.json()
        print(f"Name: {user_info.get('name')}")
        print(f"Email: {user_info.get('email')}")
        print(f"Bio: {user_info.get('bio')}")
    else:
        print(f'Failed to fetch user info. Status code: {response.status_code}')

def get_repo_data(base_url, username):
    headers = {'Authorization': f'token {token}'}
    response = requests.get(f'{base_url}/users/{username}/repos', headers=headers)

    if response.status_code == 200:
        with open('repo_data.json', 'w') as f:
            repos = response.json()
            for repo in repos:
                f.write(repo)
    else:
        print(f'Failed to fetch repository data. Status code: {response.status_code}')

def get_starred_repo_names(base_url, username):
    headers = {'Authorization': f'token {token}'}
    response = requests.get(f'{base_url}/users/{username}/starred', headers=headers)

    if response.status_code == 200:
        for repo in response.json():
            print(repo['name'])
    else:
        print(f'Failed to fetch starred repository names. Status code: {response.status_code}')

get_user_info(base_url, username)
get_repo_data(base_url, username)
get_starred_repo_names(base_url, username)
