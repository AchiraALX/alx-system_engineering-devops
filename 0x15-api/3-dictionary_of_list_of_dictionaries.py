#!/usr/bin/python3
"""
Extend the python script from exercise 0 to export data in JSON format.
Records all completed tasks from all employees.
Format must be: {"USER_ID": [ {"task": TASK_TITLE,
                               "completed": TASK_COMPLETED_STATUS,
                               "username": USERNAME"},
                               {...}
                            ]
File name must be: todo_all_employees.json
"""
import json
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url_users = "http://jsonplaceholder.typicode.com/users"
    url_todos = "http://jsonplaceholder.typicode.com/todos"

    with urllib.request.urlopen(url_users) as response:
        users = json.loads(response.read().decode())

    with urllib.request.urlopen(url_todos) as response:
        todos = json.loads(response.read().decode())

    storage = {}

    for user in users:
        eid = user.get("id")
        username = user.get("username")
        all_tasks = []

        for task in todos:
            if (task.get("userId") == eid and task.get("completed")):
                temp = {}
                temp["task"] = task.get("title")
                temp["completed"] = task.get("completed")
                temp["username"] = username
                all_tasks.append(temp)

        storage[eid] = all_tasks

    with open("todo_all_employees.json", 'w+') as jsonfile:
        json.dump(storage, jsonfile)
