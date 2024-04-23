import requests
import json
import jsonpath


def test_add_new_student():
    url = 'https://thetestingworldapi.com/api/studentsDetails'
    file = open('C:\\Users\\Admin\\Desktop\\studentdetail.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post(url, json_request)
    print(response.text)


def test_update_new_student():
    url = 'https://thetestingworldapi.com/api/studentsDetails/10098978'
    file = open('C:\\Users\\Admin\\Desktop\\studentdetail.json', 'r')
    json_request = json.loads(file.read())
    response = requests.put(url, json_request)
    print('update', response.content)
    assert response.status_code == 201


def test_get_student_data():
    url = 'https://thetestingworldapi.com/api/studentsDetails/10098978'
    response = requests.get(url)
    json_response = json.loads(response.text) # response.json() -> It will automatically convert the response into json format
    print(json_response)
    id = jsonpath.jsonpath(json_response, 'data.id')
    assert id[0] == 10098978


def test_delete_student_data():
    url = 'https://thetestingworldapi.com/api/studentsDetails/10098978'
    response = requests.delete(url)
    print(response.text)
