import requests

# Adding Header as a Dictionary
headerData = {'T1': 'First_Header', 'T2': 'Second_Header'}
url = 'https://httpbin.org/get'

response = requests.get(url, headers=headerData)
print(response.text)
