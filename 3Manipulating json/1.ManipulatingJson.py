import requests

url = 'https://restcountries.com/v3.1/all'

response = requests.get(url)

content  = response.json()

for c in content:
    print(c['name']['common'])


