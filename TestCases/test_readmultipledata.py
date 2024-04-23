import pytest
import requests
import json
from Utilities import ExcelReader


@pytest.mark.parametrize("first_name, middle_name, last_name, date_of_birth", ExcelReader.readexcelfile("StudentData"))
def test_readmultipledata(first_name, middle_name, last_name, date_of_birth):
    url = 'https://thetestingworldapi.com/api/studentsDetails'
    file = open('C:\\Users\\Admin\\Desktop\\studentdetail.json')
    json_request = json.loads(file.read())

    json_request['first_name'] = first_name
    json_request['middle_name'] = middle_name
    json_request['last_name'] = last_name
    json_request['date_of_birth'] = date_of_birth

    response = requests.post(url, json_request)
    print(response.text)
    print(response.status_code)
    assert response.status_code == 201
