#!/usr/bin/python3
'''
Returns number of subscribers for a specific subreddit
'''
def number_of_subscribers(subreddit):
    from requests import get
    headers = {'user-agent': 'user', 'allow_redirect': 'FALSE'}
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    data = get(URL, headers=headers).json()
    subdata = data.get('data')
    subscribers = subdata.get('subscribers')
    if subscribers is None:
        return 0
    return subscribers
