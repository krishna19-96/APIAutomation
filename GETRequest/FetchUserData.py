import jsonpath
import requests
import json

url = 'https://reqres.in/api/users?page=2'

response = requests.get(url)

print("normal response", response)
print("Content", response.content)
print("Text", response.text)
print("header", response.headers)
print("statuscode", response.status_code)
assert response.status_code == 200

# Fetch particular data from the response
print(response.headers.get('Date'))
print(response.headers.get('Content-Type'))
print(response.encoding)
# To check the complete time taken for the one request and response
print(response.elapsed)

json_response = json.loads(response.text)
print(json_response)

page = jsonpath.jsonpath(json_response, 'total_pages')
print(page[0])
assert page[0] == 2

for i in range(0, 6):
    first_name = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
    print(first_name[0])
