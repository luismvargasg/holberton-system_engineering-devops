#!/usr/bin/python3
"""Script that using a REST API, for a given employee ID, returns information
about his/her TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])
    r = requests.get(url)
    name = r.json().get('name')
    r = requests.get("{}/todos".format(url))
    r_list = r.json()
    completed_tasks = []
    for task in r_list:
        if task.get('completed'):
            completed_tasks.append(task)
    print("Employee {} is done with tasks({}/{}):".format(
        name, len(completed_tasks), len(r_list)))
    for title in completed_tasks:
        print("\t {}".format(title.get('title')))
