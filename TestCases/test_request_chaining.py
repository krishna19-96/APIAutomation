import json
import requests
import jsonpath


def test_add_stud():
    global id
    url = 'https://thetestingworldapi.com/api/studentsDetails'
    file =open('C:\\Users\\Admin\\Desktop\\studentdetail.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(url, request_json)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])


def test_get_detail():
    # we're getting id from previous method
    url = 'https://thetestingworldapi.com/api/studentsDetails/'+str(id[0])
    response = requests.get(url)
    print(response.text)
