#!/usr/bin/python3
"""prints titles of the first 10 hot posts listed for a given subreddit."""
import json
import requests


def top_ten(subreddit):
    """function to get first 10 post of a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'User Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for i in range(10):
            print(posts[i]['data']['title'])
    else:
        print(None)
