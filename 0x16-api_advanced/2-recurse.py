#!/usr/bin/python3
'''
Returns list of hot posts for a specific subreddit recursively
'''


def recurse(subreddit, hot_list=[]):
    from requests import get
    headers = {'user-agent': 'user'}
    URL = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    data = get(URL, headers=headers, allow_redirects=False)
    if data.status_code is not 200:
        return None
    else:
        datalist = data.json().get('data').get('children')
        subdata = datalist[len(hot_list) - 1].get('data').get('title')
        if subdata not in hot_list:
            hot_list.append(subdata)
            recurse(subreddit, hot_list)
            return hot_list
