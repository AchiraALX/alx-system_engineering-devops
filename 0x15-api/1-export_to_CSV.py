#!/usr/bin/python3
"""
This is a Python script that retrieves employee data from a mock REST API
and exports the data in CSV format. The script uses the urllib module
to make HTTP requests to the API and the sys module to retrieve command-line
arguments.
"""

import csv
import json
import urllib.request
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = f"http://jsonplaceholder.typicode.com/users/{user_id}"
    with urllib.request.urlopen(url) as response:
        username = json.loads(response.read().decode())["username"]
    all_tasks = []

    # Structure of all_tasks list:
    # [
    #   [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE],
    #   [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE],
    #   ...
    # ]

    url = "http://jsonplaceholder.typicode.com/todos"
    with urllib.request.urlopen(url) as response:
        tasks = json.loads(response.read().decode())
        for task in tasks:
            if task.get("userId") == int(user_id):
                all_tasks.append({
                    "USER_ID": user_id,
                    "USERNAME": username,
                    "TASK_COMPLETED_STATUS": task.get("completed"),
                    "TASK_TITLE": task.get("title")
                })

    with open(f"{user_id}.csv", "w+", newline="") as csvfile:
        fieldnames = [
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
        ]
        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_ALL
        )
        writer.writeheader()
        writer.writerows(all_tasks)
