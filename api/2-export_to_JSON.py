#!/usr/bin/python3
"""
 script that given employee ID, returns information
 about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/", params={"id": employee_id}).json()
    tasks = requests.get(url + "todos/", params={"userId": employee_id}).json()

    # Create JSON data
    username = user[0].get("username") if len(user) > 0 else None
    json_data = [{"task": task.get('title'),
                  "completed": task.get('completed'),
                  "username": username} for task in tasks]

    with open("{}.json".format(employee_id), "w", newline="") as jsonfile:
        json.dump({employee_id: json_data}, jsonfile)
