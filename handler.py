import os
import requests
import json
from datetime import datetime, timedelta
import urllib.parse
import time

#GITHUB_USER_NAME = ""
#GITHUB_API_TOKEN = ""
#PINBOARD_API_TOKEN = ""

def save_to_pinboard(repo):
    pinboard_api_token = os.environ.get('PINBOARD_API_TOKEN') or PINBOARD_API_TOKEN
    if repo['description']:
        description = repo['name'] + ": " + urllib.parse.quote(repo['description'])
    else:
        description =  repo['name']
    url = f"https://api.pinboard.in/v1/posts/add?auth_token={pinboard_api_token}&url={repo['html_url']}&description={description}&tags=github"
    response = requests.get(url)
    return response.status_code == 200

def fetch_starred_repos(since):
    github_user_name = os.environ.get('GITHUB_USER_NAME') or GITHUB_USER_NAME
    github_api_token = os.environ.get('GITHUB_API_TOKEN') or GITHUB_API_TOKEN
    headers = {'Authorization': f'token {github_api_token}'}
    url = f"https://api.github.com/users/{github_user_name}/starred?since={since}"
    response = requests.get(url, headers=headers)
    return response.json()

def lambda_handler(event, context):
    since = (datetime.now() - timedelta(hours=1)).isoformat()
    starred_repos = fetch_starred_repos(since)

    for repo in starred_repos[:8]:
        if save_to_pinboard(repo):
            #print(repo)
            print(f"Saved {repo['html_url']} to Pinboard")
            #return
        else:
            print(f"Failed to save {repo['html_url']}")
        time.sleep(.25)  # Add a one-second delay
    return {
        'statusCode': 200,
        'body': json.dumps('Execution completed')
    }

#lambda_handler(None, None)
