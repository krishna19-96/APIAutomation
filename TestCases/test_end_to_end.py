import pytest
import json
import jsonpath
import requests


def test_end_to_end():
    url = 'https://thetestingworldapi.com/api/studentsDetails'
    file =open('C:\\Users\\Admin\\Desktop\\studentdetail.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post(url,json_request)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_api_url = 'https://thetestingworldapi.com/api/technicalskills'
    file = open('C:\\Users\\Admin\\Desktop\\addtechskill.json', 'r')
    json_request = json.loads(file.read())
    json_request['id'] = int(id[0])
    json_request['st_id'] = id[0]
    response = requests.post(tech_api_url, json_request)
    print("Tech" , response.text)

    add_api_url = 'https://thetestingworldapi.com/api/addresses'
    file = open('C:\\Users\\Admin\\Desktop\\addaddrs.json', 'r')
    json_request = json.loads(file.read())
    json_request['stId'] = id[0]
    response = requests.post(add_api_url, json_request)

    final_api_url = 'https://thetestingworldapi.com/api/FinalStudentDetails/'+str(id[0])
    response = requests.get(final_api_url)
    print("final", response.text)


