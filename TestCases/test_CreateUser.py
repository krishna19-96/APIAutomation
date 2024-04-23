import jsonpath
import requests
import json
import pytest


url = 'https://reqres.in/api/users'

@pytest.fixture()
def start_first():
    global file
    file = open('C:\\Users\\Admin\\Desktop\\CreateUser.json', 'r')

@pytest.mark.Smoke
def test_create_user(start_first):
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    assert response.status_code == 201

@pytest.mark.Sanity
# @pytest.mark.skip(reason= "not done yet")
def test_create_user1(start_first):
    file = open('C:\\Users\\Admin\\Desktop\\CreateUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    json_response = json.loads(response.content)
    final_response = jsonpath.jsonpath(json_response, 'id')
    print(final_response[0])
