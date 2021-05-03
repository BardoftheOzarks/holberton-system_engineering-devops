#!/usr/bin/python3
'''
Retrieves info from a REST API
'''

if __name__ == "__main__":
    import csv
    from requests import get
    from sys import argv

    URL = 'https://jsonplaceholder.typicode.com'
    username = get(URL + '/users/' + argv[1]).json().get('username')
    tasks = get(URL + '/users/' + argv[1] + '/todos').json()

    with open('{}.csv'.format(argv[1]), 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            row = []
            row.append(argv[1])
            row.append(username)
            row.append(task.get('completed'))
            row.append(task.get('title'))
            writer.writerow(row)
