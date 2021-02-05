#!/usr/bin/python3
'''
Returns list of hot posts for a specific subreddit recursively
'''


def recurse(subreddit, hot_list=[], after=None):
    from requests import get
    headers = {'user-agent': 'user'}
    URL = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    data = get(URL,
               headers=headers,
               allow_redirects=False,
               params={'after': after})
    if data.status_code is not 200:
        return None
    else:
        datalist = data.json().get('data').get('children')
        for entry in datalist:
            subdata = entry.get('data').get('title')
            hot_list.append(subdata)
        after = data.json().get('data').get('after')
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list


def count_words(subreddit, word_list):
    hot_list = recurse(subreddit)
    word_list = format_words(word_list)
    if hot_list is None:
        return
    elif hot_list:
        print_counts(hot_list, word_list)
    else:
        count_words(subreddit, word_list)


def format_words(word_list):
    new_list = []
    for word in word_list:
        if word.lower() not in new_list:
            new_list.append(word.lower())
    return new_list


def print_counts(hot_list, word_list):
    counts = {}
    for word in word_list:
        count = 0
        for entry in hot_list:
            if word in entry.lower().split():
                count += 1
        if word in counts:
            counts[word] += count
        else:
            counts[word] = count
    for key, val in sorted(counts.items()):
        if val > 0:
            print('{}: {}'.format(key, val))
