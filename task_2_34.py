import json

import requests


def get(url):
    request = requests.get(url, params={"subreddit": "TheSimsBuilding", "sort": "desc", "sort_type": "created_utc"})
    return request.json()


def write(data):
    with open('comment.json', 'w') as f:
        json.dump(data, f, indent=4)


def main():
    url = 'https://api.pushshift.io/reddit/comment/search/'
    data = get(url)
    write(data)


main()
