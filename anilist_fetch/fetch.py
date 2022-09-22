'''
Utilities for fetching data from Anilist via their GraphQL API.
'''
import csv
import json
import os
import re
import time
import traceback
from datetime import datetime, timedelta
import requests

ANILIST_API = 'https://graphql.anilist.co'
TIMEOUT_SECS = 30
RATE_LIMIT_WAIT = 1.75 # (90 requests / 60) + padding
PER_PAGE = 50


def to_fuzzy_date_int(dt: datetime) -> int:
    '''
    Convert datetime to FuzzyDateInt.

    Anilist GraphQL Docs:
      8 digit long date integer (YYYYMMDD).
      Unknown dates represented by 0. E.g. 2016: 20160000, May 1976: 19760500
    '''
    return int(dt.strftime('%Y%m%d'))


def anilist_date_to_str(ad: dict) -> str:
    '''
    Convert Anilist date from {'year': 2022, 'month' 09, 'day': 01} to '2022-09-01'
    '''
    y = ad['year'] if ad['year'] else 1900
    m = ad['month'] if ad['month'] else 1
    d = ad['day'] if ad['day'] else 1
    return f'{y}-{m:02d}-{d:02d}'


def clean_description(desc: str) -> str:
    '''
    Cleans Anilist anime entry description of HTML and other junk.
    
    Note: I tried to use the flag to disable HTML in Anilist's API,
        but it didn't seem to do a thing? 
    '''
    if desc:
        return re.sub('<[^<]+?>', '', desc).replace('\n','')
    return None


def anime_entry_to_row(entry: dict) -> list:
    '''
    Convert Anilist anime entry to CSV row.
    Nested objects are serialized to JSON strings.
    '''
    try:
        return [
            entry['id'],
            entry['title']['english'],
            entry['title']['romaji'],
            entry['title']['native'],
            entry['type'],
            entry['format'],
            entry['status'],
            clean_description(entry['description']),
            anilist_date_to_str(entry['startDate']),
            anilist_date_to_str(entry['endDate']),
            entry['season'],
            entry['seasonYear'],
            entry['seasonInt'],
            entry['episodes'],
            entry['duration'],
            entry['countryOfOrigin'],
            json.dumps(entry['genres']),
            entry['averageScore'],
            entry['meanScore'],
            entry['popularity'],
            entry['source'],
            entry['nextAiringEpisode'],
            json.dumps(entry['tags']),
            json.dumps(entry['studios']['nodes']),
        ]
    except Exception as e:
        print(f'error mapping anime entry to row.\n{entry}')
        traceback.print_exc()
    

def gql_src(gql_path: str) -> str:
    '''
    Opens GraphQL file source
    '''
    this_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(this_dir, gql_path), encoding='utf-8') as gql_file:
        return re.sub(r'\s+', ' ', ''.join(gql_file.readlines()))


def anilist_req(gql_src: str, gql_vars: dict):
    '''
    Generic Anilist GraphQL request with query and variables.
    '''
    headers = {'Content-Type': 'application/json'}
    body = {'query': gql_src, 'variables': gql_vars}
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


def get_anime(anime_id: int) -> dict:
    '''
    Fetches single Anilist anime entry
    '''
    return anilist_req(gql_src('gql/anime_single.gql'), {'id': anime_id})['data']['Media']


def download_anime_range(start: datetime, end: datetime, out_csv: str) -> int:
    '''
    Downloads all Anilist anime data in date range (YYYYMMDD-YYYYMMDD) to CSV.
    Returns entry count.

    Note: This will batch requests to avoid hitting Anilist's rate limit. So, the
        bigger the range, the longer the download.
    '''
    gql_vars = {
        'page': 1,
        'perPage': PER_PAGE,
        'startDate': to_fuzzy_date_int(start),
        'endDate': to_fuzzy_date_int(end + timedelta(1))
    }
    header = [
        'id', 'title_english', 'title_romaji', 'title_native', 'type', 'format', 'status', 'description', 
        'startDate', 'endDate', 'season', 'seasonYear', 'seasonInt', 'episodes', 'duration_mins', 'countryOfOrigin', 
        'genres', 'averageScore', 'meanScore', 'popularity', 'source', 'nextAiringEpisode', 'tags', 'studios'
    ]
    with open(out_csv, 'w+', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        # batch request all Anilist entries, page by page without hitting API limit
        idx = 1
        while True:
            print(f"\rDownloading page {gql_vars['page']} => Entries {idx}-{idx + PER_PAGE - 1}", end='')
            data = anilist_req(gql_src('gql/anime_range.gql'), gql_vars)['data']
            entries = data['Page']['media']
            for entry in entries:
                writer.writerow(anime_entry_to_row(entry))

            # setup for next page
            if not data['Page']['pageInfo']['hasNextPage']:
                break
            time.sleep(RATE_LIMIT_WAIT)
            gql_vars['page'] += 1
            idx += len(entries)
        return idx
