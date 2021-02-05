#!/usr/bin/python3
'''
Returns top ten posts for a specific subreddit
'''


def top_ten(subreddit):
    from requests import get
    headers = {'user-agent': 'user'}
    URL = 'https://www.reddit.com/r/{}/top/.json'.format(subreddit)
    data = get(URL, headers=headers, allow_redirects=False)
    if data.status_code is not 200:
        print('None')
    else:
        datalist = data.json().get('data').get('children')
        count = 0
        while count < 10:
            subdata = datalist[count].get('data').get('title')
            print(subdata)
            count += 1
