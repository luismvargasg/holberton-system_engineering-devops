#!/usr/bin/python3
"""Script that using a REST API, for a given employee ID, returns information
about his/her TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    r = requests.get(url)
    username = r.json().get('username')
    r = requests.get("{}/todos".format(url))
    r_list = r.json()
    with open('{}.csv'.format(id), 'w') as file:
        for item in r_list:
            file.write('"{}","{}","{}","{}"\n'
                       .format(id, username, item.get('completed'),
                               item.get('title')))
