#!/usr/bin/python3
'''
Returns list of hot posts for a specific subreddit recursively
'''


def recurse(subreddit, hot_list=[], after=None):
    from requests import get
    headers = {'user-agent': 'user'}
    URL = 'https://www.reddit.com/r/{}/hot/.json?after={}'.format(subreddit,
                                                                  after)
    data = get(URL, headers=headers, allow_redirects=False,)
    if data.status_code is not 200:
        return None
    else:
        datalist = data.json().get('data').get('children')
        for entry in datalist:
            subdata = entry.get('data').get('title')
            if subdata not in hot_list:
                hot_list.append(subdata)
        after = data.json().get('data').get('after')
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
