#!/usr/bin/python3
'''
Retrieves info from a REST API
'''
if __name__ == "__main__":
    from requests import get
    from sys import argv
    URL = 'https://jsonplaceholder.typicode.com'
    name = get(URL + '/users/' + argv[1]).json().get('name')
    tasks = get(URL + '/users/' + argv[1] + '/todos').json()
    done = []
    for task in tasks:
        if task.get('completed') is True:
            done.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(
        name, len(done), len(tasks)))
    if len(done) > 0:
        for task in done:
            print('\t {}'.format(task))
