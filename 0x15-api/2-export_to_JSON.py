#!/usr/bin/python3
"""
Extend the python script from exercise 0 to export data in JSON format.
Record all tasks that are owned by the employee.
Format must be: {"USER_ID": [ {"task": TASK_TITLE,
                               "completed": TASK_COMPLETED_STATUS,
                               "username": USERNAME"},
                               {...}
                            ]
File name must be: USER_ID.json
"""
import json
import sys
from urllib.request import urlopen

if __name__ == "__main__":
    eid = sys.argv[1]
    with urlopen(f"http://jsonplaceholder.typicode.com/users/{eid}") as response:
        username = json.loads(response.read().decode())["username"]
    all_tasks = []
    with urlopen("http://jsonplaceholder.typicode.com/todos") as response:
        r = json.loads(response.read().decode())
        for task in r:
            if task.get("userId") == int(eid):
                temp = {}
                temp["task"] = task.get("title")
                temp["completed"] = task.get("completed")
                temp["username"] = username
                all_tasks.append(temp)

    with open(f"{eid}.json", "w+") as jsonfile:
        json.dump({eid: all_tasks}, jsonfile)
