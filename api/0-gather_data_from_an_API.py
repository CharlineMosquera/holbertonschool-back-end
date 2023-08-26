#!/usr/bin/python3
"""
 script that given employee ID, returns information
 about his/her TODO list progress.
"""
import json
import sys
from urllib import request, error

if __name__ == '__main__':
    employee_id = sys.argv[1]

    # Get employee information
    url_user = "https://jsonplaceholder.typicode.com/users/"
    with request.urlopen(f"{url_user}{employee_id}")as response:
        employee_data = json.loads(response.read().decode())
        employee_name = employee_data['name']

    # Get todo list
    url_userid = "https://jsonplaceholder.typicode.com/todos?userId="
    with request.urlopen(f"{url_userid}{employee_id}") as response:
        todos = json.loads(response.read().decode())

    # Count completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]
    done_tasks = len(completed_tasks)
    total = len(todos)

    # Print output
    tasks_message = f'tasks({done_tasks}/{total}):'
    print("Employee {} is done with {}".format(employee_name, tasks_message))
    [print("\t {}".format(todo["title"])) for todo in completed_tasks]
