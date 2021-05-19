#!/usr/bin/python3
'''queries the Reddit API'''
import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''returns list of hot posts recursively'''
    if after is None:
        response = requests.get('https://api.reddit.com/r/{}/hot'
                                .format(subreddit),
                                headers={'user-agent': 'Excelsior'},
                                allow_redirects=False).json()
    else:
        response = requests.get('https://api.reddit.com/r/{}/hot?after={}'
                                .format(subreddit, after),
                                headers={'user-agent': 'Excelsior'},
                                allow_redirects=False).json()
    if 'data' not in response and hot_list == []:
        return None
    data = response.get('data')
    children = data.get('children')
    for child in children:
        subdata = child.get('data')
        title = subdata.get('title')
        hot_list.append(title)
    after = data.get('after')
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
