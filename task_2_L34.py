import json

import requests


def get_comment(URL, par):
    data = requests.get(URL, params=par)
    return data.json()


def write_to_file(data):
    with open('comments.json', 'w') as file:
        json.dump(data['data'], file, indent=4)


def main():
    global value
    URL = 'https://api.pushshift.io/reddit/comment/search/'
    par = {'subreddit': 'TheSimsBuilding', 'sort': 'desc', 'sort_type': 'created_utc'}
    data = get_comment(URL=URL, par=par)
    write_to_file(data)


if __name__ == '__main__':
    main()
