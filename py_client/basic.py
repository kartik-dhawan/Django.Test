import requests

endpoint = 'https://httpbin.org/anything'

res = requests.get(endpoint, json={'name': 'bond'})
print(res.json())
