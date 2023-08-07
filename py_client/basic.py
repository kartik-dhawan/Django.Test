import requests

endpoint = 'http://localhost:8000/api/books/'

res = requests.get(endpoint, params={'id': 12}, json={'name': 'bond'})
print(res.json())
