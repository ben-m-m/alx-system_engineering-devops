#!/usr/bin/python3
"""queries Reddit API"""
import json
import requests


def number_of_subscribers(subreddit):
    """function that gets number of subscribers to a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'User Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data").get("subscribers")
        return data
    else:
        return 0
