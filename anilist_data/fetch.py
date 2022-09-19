'''
Utilities for fetching data from Anilist via their GraphQL API.
'''
import os
import re
import requests

ANILIST_API = 'https://graphql.anilist.co'
TIMEOUT_SECS = 30
PER_PAGE = 50

def gql_src(gql_path: str) -> str:
    '''
    Opens GraphQL file source
    '''
    this_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(this_dir, gql_path), encoding='utf-8') as gql_file:
        return re.sub(r'\s+', ' ', ''.join(gql_file.readlines()))

def anilist_req(gql: str, variables: dict):
    '''
    Generic Anilist GraphQL request with query and variables.
    '''
    headers = {'Content-Type': 'application/json'}
    body = {
        'query': gql,
        'variables': variables
    }
    resp = requests.post(ANILIST_API, headers=headers, json=body, timeout=TIMEOUT_SECS)
    if resp.status_code != 200:
        raise Exception('Failed to request Anilist data.\nRequest body: '
            f'{body}\n{resp.status_code} {resp.content}')
    return resp.json()

def get_user(user_id: int) -> dict:
    '''
    Fetches Anilist user data
    '''
    data = anilist_req(gql_src('gql/user.gql'), {'id': user_id})['data']
    return {'user': data['User'], 'lists': data['MediaListCollection']['lists']}

# fetch anime data
def get_anime(anime_id: int) -> dict:
    '''
    Fetches single Anilist anime entry
    '''
    return anilist_req(gql_src('gql/anime_single.gql'), {'id': anime_id})['data']['Media']

def download_anime_range(start: int, end: int, out_csv: str) -> int:
    '''
    Downloads all Anilist anime data in date range (YYYYMMDD-YYYYMMDD) to CSV; Returns entry count
    '''
