import json

import requests


def get_data(url):
    data = requests.get(url)
    return data.json()


def write_to_file(data):
    with open("comments.json", 'w') as file:
        json.dump(data, file, indent=4)

def main():
    url = ''
