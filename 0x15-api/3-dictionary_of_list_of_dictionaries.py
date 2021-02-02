#!/usr/bin/python3
'''
Retrieves info from a REST API
'''

if __name__ == "__main__":
    from json import dumps
    from requests import get

    URL = 'https://jsonplaceholder.typicode.com'
    userlist = get(URL + '/users/').json()
    user_dict = {}
    for user in userlist:
        username = get(URL + '/users/' +
                       str(user["id"])).json().get('username')
        tasks = get(URL + '/users/' + str(user["id"]) + '/todos').json()
        todo_list = []
        for task in tasks:
            task_dict = {}
            task_dict["task"] = task.get('title')
            task_dict["completed"] = task.get('completed')
            task_dict["username"] = "{}".format(username)
            todo_list.append(task_dict)
        user_dict[str(user["id"])] = todo_list

    with open('todo_all_employees.json', 'w') as file:
        file.write(dumps(user_dict))
