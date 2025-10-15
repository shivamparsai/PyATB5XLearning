# create Token Req

import allure
import pytest
import requests

base_url = "https://restful-booker.herokuapp.com"
headers = {
    "Content-Type": "application/json"
}

def test_create_token():
    path_url = "/auth"
    fullurl = base_url + path_url
    json_payload_auth = {
        "username" : "admin",
        "password" : "password123"
    }

    resposeData = requests.post(url=fullurl, headers=headers, json=json_payload_auth)

    print(resposeData)

    assert resposeData.status_code == 200

    responseDataJson = resposeData.json()
    print(resposeData.text)
    token = responseDataJson["token"]
    print(token)