#!/usr/bin/python3
"""
This is a Python script that retrieves employee data from a mock REST API
and outputs the number of tasks completed by the employee, as well as the
titles of the completed tasks. The script uses urllib to make HTTP requests
to the API and the sys module to retrieve command-line arguments.
"""

import sys
import urllib.request
import json


if __name__ == "__main__":
    # Get employee ID from command-line argument
    eid = sys.argv[1]

    # Retrieve employee name from API
    with urllib.request.urlopen(
        "http://jsonplaceholder.typicode.com/users/{}".format(eid)
    ) as response:
        data = json.loads(response.read().decode())
        name = data.get("name")

    # Count completed tasks for employee
    total_tasks = 0
    done_tasks = []
    with urllib.request.urlopen(
        "http://jsonplaceholder.typicode.com/todos"
    ) as response:
        data = json.loads(response.read().decode())
        for task in data:
            if task.get("userId") == int(eid):
                total_tasks += 1
                if task.get("completed"):
                    done_tasks.append(task.get("title"))

    # Output results
    print(
        "Employee {} is done with tasks({}/{}):".format(name, len(done_tasks),
                                                        total_tasks)
    )
    for item in done_tasks:
        print("\t{}".format(item))
