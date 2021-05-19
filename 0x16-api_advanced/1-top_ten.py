#!/usr/bin/python3
'''queries the Reddit API'''
import json
import requests


def top_ten(subreddit):
    '''prints top ten posts'''
    response = requests.get('https://api.reddit.com/r/{}/hot?limit=10'
                            .format(subreddit),
                            headers={'user-agent': 'Excelsior'},
                            allow_redirects=False).json()
    if 'data' not in response:
        print('None')
        return
    data = response.get('data')
    children = data.get('children')
    for child in children:
        subdata = child.get('data')
        title = subdata.get('title')
        print(title)
