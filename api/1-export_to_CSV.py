#!/usr/bin/python3
"""
 script that export data in the CSV format
"""
import csv
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]

    # Get employee information
    url_users = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(f"{url_users}{employee_id}")
    employee_data = response.json()
    employee_name = employee_data['username']

    # Get todo list
    url_list = "https://jsonplaceholder.typicode.com/todos?userId="
    response = requests.get(f"{url_list}{employee_id}")
    todos = response.json()

    # Count completed tasks
    completed_tasks = []
    for todo in todos:
        if todo['completed']:
            completed_tasks.append(todo)

    # Write CSV file
    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([todo['userId'],
                             employee_name, todo['completed'], todo['title']])
