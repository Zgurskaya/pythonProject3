import requests
import json

url = 'https://api.github.com'
user = 'Zgurskaya'
response = requests.get(f'{url}/users/{user}/repos')

with open('file.json', 'w') as f:
    json.dump(response.json(), f)

for i in response.json():
    print(i['name'])
