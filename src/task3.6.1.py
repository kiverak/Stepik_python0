import requests

with open('text.txt', 'r') as inf:
    url = inf.readline().strip()
print(len(requests.get(url).text.splitlines()))