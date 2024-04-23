import jsonpath
import requests
import json

url = 'https://reqres.in/api/users/2'

file = open('C:\\Users\\Admin\\Desktop\\CreateUser.json', 'r')

json_input = file.read()
# print(type(json_input))
request_json = json.loads(json_input)
# print(type(request_json))

# Make a Put request with Json input body
response = requests.put(url, request_json)

# Validate the Response code
assert response.status_code == 200, "Fail"

# print(response.content)

#Json path
json_response = json.loads(response.content)
response = jsonpath.jsonpath(json_response,'updatedAt')
print(response[0])
