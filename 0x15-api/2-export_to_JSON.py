#!/usr/bin/python3
'''
Retrieves info from a REST API
'''

if __name__ == "__main__":
    from json import dumps
    from requests import get
    from sys import argv

    URL = 'https://jsonplaceholder.typicode.com'
    username = get(URL + '/users/' + argv[1]).json().get('username')
    tasks = get(URL + '/users/' + argv[1] + '/todos').json()
    todo_list = []
    for task in tasks:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = "{}".format(username)
        todo_list.append(task_dict)
    user_dict = {argv[1]: todo_list}

    with open('{}.json'.format(argv[1]), 'w') as file:
        file.write(dumps(user_dict))
