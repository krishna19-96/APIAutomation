import json

import requests
from requests.auth import HTTPBasicAuth


def test_authentication():
    url = 'https://github.com/login'
    response = requests.get(url, auth=HTTPBasicAuth('krish19296@gmail.com','krishnagit19@@'))
    print(response.content)

