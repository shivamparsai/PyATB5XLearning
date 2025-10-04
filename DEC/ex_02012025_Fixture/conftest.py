import pytest
import allure
import requests
from dotenv import load_dotenv
import os


@pytest.fixture()
def get_token():
    load_dotenv()
    username = os.getenv("USERNAME1")
    password = os.getenv("PASSWORD")
    print(username, password)

    url = "https://restful-booker.herokuapp.com/auth"
    headers = {
        "Content-Type" : "application/json"
    }
    payload = {
        "username" : username,
        "password" : password
    }

    response = requests.post(url=url, headers=headers, json=payload)
    responseJsonData = response.json()
    print(response.text)
    token = responseJsonData["token"]
    print("from conftest", token)
    return token


@pytest.fixture()
def get_booking_id():
    url = "https://restful-booker.herokuapp.com/booking"
    header = {
        "Content-Type" : "application/json"
    }
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=url, headers=header, json=payload)
    booking_id = response.json()["bookingid"]
    print("from conftest",booking_id)
    return booking_id



