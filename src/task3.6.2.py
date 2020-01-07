import requests

with open('text.txt', 'r') as inf:
    url = inf.readline().strip()
s = 'https://stepic.org/media/attachments/course67/3.6.3/'

while True:
    r = requests.get(url).text
    if r.split()[0] == 'We':
        r = requests.get(url).text
        break
    url = s + r
    print(url)
print(r)