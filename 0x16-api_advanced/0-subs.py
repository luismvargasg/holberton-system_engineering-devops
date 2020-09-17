#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers
for a given subreddit. If an invalid subreddit is given, the function should
return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Function that returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    subs = r.json().get('data').get('subscribers')
    return subs
