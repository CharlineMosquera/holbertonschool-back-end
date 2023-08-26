#!/usr/bin/python3
"""
script that given employee ID, returns information
about his/her TODO list progress.
"""
import json
import sys
from urllib import request, error

if __name__ == '__main__':
    url_user = "https://jsonplaceholder.typicode.com/users/"
    url_userid = "https://jsonplaceholder.typicode.com/todos?userId="
    all_todos = {}

    # Loop over all users
    for user_id in range(1, 11):
        # Get employee information
        with request.urlopen(f"{url_user}{user_id}")as response:
            employee_data = json.loads(response.read().decode())
            employee_name = employee_data['name']

        # Get todo list
        with request.urlopen(f"{url_userid}{user_id}") as response:
            todos = json.loads(response.read().decode())

        # Store tasks for current user
        task_list = []
        for todo in todos:
            task = {
                "username": employee_data['username'],
                "task": todo['title'],
                "completed": todo['completed']
            }
            task_list.append(task)

        # Store tasks for current user in all_todos dictionary
        all_todos[user_id] = task_list

    # Write all_todos to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_todos, json_file)
