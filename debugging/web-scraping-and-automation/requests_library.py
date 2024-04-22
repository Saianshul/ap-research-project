import requests
from requests.auth import HTTPBasicAuth

base_url = 'https://api.github.com'
username = 'Saianshul1026'

def get_user_info(base_url, username):
    token = 'token'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(f'{base_url}/users/{username}', headers=headers, timeout=1)

    if response.status_code == 200:
        print(f"Name: {response.json().get('name')}")
        print(f"Email: {response.json().get('email')}")
        print(f"Bio: {response.json().get('bio')}")
    else:
        print(f'Failed to fetch user info. Status code: {response.status_code}')

def get_repo_data(base_url, username):
    auth = HTTPBasicAuth('example@gmail.com', 'password')
    response = requests.get(f'{base_url}/users/{username}/repos', auth=auth)

    if response.status_code == 200:
        with open('repo_data.json', 'w') as f:
        # with open('repo_data.json', 'wb') as f:
            for data in response.iter_content():
                f.write(data)
    else:
        print(f'Failed to fetch repository data. Status code: {response.status_code}')

def get_starred_repo_names(base_url, username):
    proxies = {
        'http': 'http://ip:port',
        # 'https': 'http://ip:port'
    }
    
    session = requests.Session()
    session.proxies.update()
    # session.proxies.update(proxies)
    response = session.get(f'{base_url}/users/{username}/starred')

    if response.status_code == 200:
        for repo in response.json():
            print(repo['name'])
    else:
        print(f'Failed to fetch starred repository names. Status code: {response.status_code}')

get_user_info(base_url, username)
get_repo_data(base_url, username)
get_starred_repo_names(base_url, username)