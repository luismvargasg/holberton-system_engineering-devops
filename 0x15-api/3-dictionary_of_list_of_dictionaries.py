#!/usr/bin/python3
"""Script that using a REST API, for all employees ID, returns information
about his/her TODO list progress inside a JSON file"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    r = requests.get(url)
    for user in range(1, len(r.json()) + 1):
        res = requests.get("{}/{}".format(url, user))
        username = res.json().get('username')
        res = requests.get("{}/{}/todos".format(url, user))
        r_list = res.json()
        my_list = []
        json_dict = {}
        for task in r_list:
            my_dict = {}
            my_dict['task'] = task.get('title')
            my_dict['completed'] = task.get('completed')
            my_dict['username'] = username
            my_list.append(my_dict)
        json_dict[user] = my_list
        with open('todo_all_employees.json', 'a') as file:
            json.dump(json_dict, file)
