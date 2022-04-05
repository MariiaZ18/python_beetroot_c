import requests

url = 'https://en.wikipedia.org/wiki/Ukraine'

resp = requests.get(url)

with open('robots.txt', 'w', encoding='utf-8') as file:
    file.write(resp.text)
