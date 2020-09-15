#!/usr/bin/python3
"""Script that using a REST API, for all employees ID, returns information
about his/her TODO list progress inside a JSON file"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    r = requests.get(url)
    json_dict = {}
    for user_id in range(1, len(r.json()) + 1):
        json_dict[user_id] = []
        user_res = requests.get("{}/{}".format(url, user_id))
        username = user_res.json().get('username')
        task_res = requests.get("{}/{}/todos".format(url, user_id))
        task_res_list = task_res.json()
        my_list = []
        for task in task_res_list:
            my_dict = {}
            my_dict['username'] = username
            my_dict['task'] = task.get('title')
            my_dict['completed'] = task.get('completed')
            my_list.append(my_dict)
        json_dict[user_id] = my_list
    with open('todo_all_employees.json', 'w') as file:
        json.dump(json_dict, file)
