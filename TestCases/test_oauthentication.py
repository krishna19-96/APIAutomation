import requests
import json
import jsonpath


def test_oauthentication():
    url = 'https://thetestingworldapi.com/Token'
    data = {'grant_type': 'password', 'username': 'admin', 'password': 'adminpass'}
    response = requests.post(url, data)
    token_value = jsonpath.jsonpath(response.json(), 'access_token')

    auth = {'Authorization': 'Bearer ' + token_value[0]}
    print(auth)
    api_url = 'https://thetestingworldapi.com/api/StDetails/1104'
    response = requests.get(api_url, headers=auth)
    print(response)
    print(response.text)
