#!/usr/bin/python3
'''queries the Reddit API'''
from requests import get


def number_of_subscribers(subreddit):
    '''returns number of subscribers'''
    response = get('https://api.reddit.com/r/{}/about.json'
                   .format(subreddit),
                   headers={'user-agent': 'Excelsior'},
                   allow_redirects=False).json()
    if 'data' not in response:
        return 0
    data = response.get('data')
    subscribers = data.get('subscribers')
    return subscribers
