#!/usr/bin/python3
"""Script that using a REST API, for a given employee ID, returns information
about his/her TODO list progress inside a JSON file"""
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    r = requests.get(url)
    username = r.json().get('username')
    r = requests.get("{}/todos".format(url))
    r_list = r.json()
    my_list = []
    my_dict = {}
    json_dict = {}
    for task in r_list:
        my_dict['task'] = task.get('title')
        my_dict['completed'] = task.get('completed')
        my_dict['username'] = username
        my_list.append(my_dict)
    json_dict[id] = my_list
    with open('{}.json'.format(id), 'w') as file:
        json.dumps(json_dict, file)
