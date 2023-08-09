#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit),
    headers = {'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}.json()
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
