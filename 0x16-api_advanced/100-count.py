#!/usr/bin/python3
'''queries the Reddit API'''
import json
import requests


def count_words(subreddit, word_list, after=None, counts={}):
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
    for word in word_list:
        word = word.lower()
        if word not in counts.keys():
            counts[word] = 0
    data = response.get('data')
    children = data.get('children')
    for child in children:
        subdata = child.get('data')
        title = subdata.get('title')
        title = title.split()
        for word in word_list:
            for title_word in title:
                if word.lower() == title_word.lower():
                    counts[word] += title.count(word)
    after = data.get('after')
    if after is None:
        results = []
        for key, value in sorted(counts.items(), key=lambda item: item[1]):
            if value != 0:
                results.append('{}: {}'.format(key, value))
        x = len(results)
        while x > 0:
            x -= 1
            print(results[x])
        return
    return count_words(subreddit, word_list, after, counts)
