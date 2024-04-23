import jsonpath
import requests
import json

url = 'https://reqres.in/api/users'

file = open('C:\\Users\\Admin\\Desktop\\CreateUser.json', 'r')

json_input = file.read()
# print(type(json_input))
request_json = json.loads(json_input)
# print(type(request_json))

# Make a post request with Json input body
response = requests.post(url, request_json)

# Validate the Response code
assert response.status_code == 201, "Fail"

# Fetch Header from Response
print(response.headers.get('Content-Length'))

print(response.content)

# pass jsonpath

response_json = json.loads(response.content)
json_response = jsonpath.jsonpath(response_json,'id')
print(json_response[0])