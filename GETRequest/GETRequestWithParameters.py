import requests

param = {'name': 'krish', 'email': 'krish111@gmail.com', 'id': '423'}

url = 'https://httpbin.org/get'

response = requests.get(url, params=param)
print(response.text)
