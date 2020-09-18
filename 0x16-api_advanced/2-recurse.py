#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """Function that returns the list of titles"""
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
                                                                 subreddit,
                                                                 after)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    after = r.json().get('data').get('after')
    if r.status_code == 200:
        response = r.json().get('data').get('children')
        for index in response:
            hot_list.append(index.get('data').get('title'))
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
