from typing import List
from datetime import datetime
import requests


def get_all_repositories():
    response = requests.get('https://api.github.com/users/pedropst/repos')
    return response.json()

def filter(repository:dict, key:str):
    return repository[key]

def order_by(repositories:List[dict], key:str, reverse:bool):
    if key == 'updated_at':
        return sorted(repositories, key=lambda x: datetime.strptime(x['updated_at'], '%Y-%m-%dT%H:%M:%SZ'), reverse=reverse)
    elif key == 'name':
        return sorted(repositories, key=lambda x: x['name'].lower(), reverse=reverse)

def search(repositories:List[dict], keyword:str):
    return [repository for repository in repositories if keyword.lower() in repository['name'].lower()]

def archived(repository:dict):
    return repository['archived']