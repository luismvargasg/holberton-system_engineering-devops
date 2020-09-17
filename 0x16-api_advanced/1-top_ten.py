#!/usr/bin/python3
"""Function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Function that returns the top ten posts"""
    url = "https://www.reddit.com/r/{}/top.json".format(subreddit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        response = r.json().get('data').get('children')
        for item in range(10):
            print(response[item].get('data').get('title'))
    else:
        print('None')
