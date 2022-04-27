# Requests using multiprocessing
import json

import requests


def get_comment(URL, par):
    data = requests.get(URL, params=par)
    return data.json()


def write_to_file(data):
    with open('comments.json', 'w') as file:
        json.dump(data['data'], file, indent=4)


def main():
    URL = 'https://api.pushshift.io/reddit/comment/search/'
    par = {'subreddit': 'TheSimsBuilding', 'sort': 'desc', 'sort_type': 'created_utc'}
    data = get_comment(URL=URL, par=par)
    write_to_file(data)


def print_comm():
    URL = 'https://api.pushshift.io/reddit/comment/search/'
    par = {'subreddit': 'TheSimsBuilding', 'sort': 'desc', 'sort_type': 'created_utc'}
    data = get_comment(URL=URL, par=par)
    new_list = []
    list_of_dict = data.get('data')
    for dictionary in list_of_dict:
        body = dictionary.get("body")
        new_list.append(body)
    for s in new_list:
        print(s, end='\n')


if __name__ == '__main__':
    main()
    print_comm()
