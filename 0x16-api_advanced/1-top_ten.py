#!/usr/bin/python3
'''queries the Reddit API'''
from requests import get


def top_ten(subreddit):
    '''returns number of subscribers'''
    response = get('https://api.reddit.com/r/{}/top?limit=10'
                   .format(subreddit),
                   headers={'user-agent': 'Excelsior'},
                   allow_redirects=False).json()
    if 'data' not in response:
        return 0
    data = response.get('data')
    children = data.get('children')
    for child in children:
        subdata = child.get('data')
        title = subdata.get('title')
        print(title)
