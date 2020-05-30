

import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'year':5})

print(r.json())
