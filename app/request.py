import requests

url = 'http://localhost:5000/results'

values = [[-0.86873684, -0.14134896,  0.33981747]]


r = requests.post(url,json=values)


print(r.json())