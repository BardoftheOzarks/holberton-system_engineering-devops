#!/usr/bin/python3
'''
Returns number of subscribers for a specific subreddit
'''


def number_of_subscribers(subreddit):
    from requests import get
    headers = {'user-agent': 'user'}
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    data = get(URL, headers=headers, allow_redirects=False)
    if data.status_code is not 200:
        return 0
    subdata = data.json().get('data')
    subscribers = subdata.get('subscribers')
    return subscribers
