import allure
import pytest
import requests

base_url = "https://restful-booker.herokuapp.com"
headers = {
    "Content-Type" : "application/json"
}

def get_token():
    path_url = "/auth"
    full_url = base_url + path_url
    json_payload_auth = {
        "username" : "admin",
        "password" : "password123"
    }

    responseData = requests.post(url=full_url, headers=headers, json=json_payload_auth)

    print("response data is ", responseData)

    responseJsonData = responseData.json()
    token = responseJsonData["token"]

    print("token is ", token )
    return token

def get_booking_id():
    path_url = "/booking"
    full_url = base_url + path_url
    print("booking api url is ", full_url)

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
    responseData = requests.post(url=full_url, headers=headers, json=payload)
    print("response data is", responseData)
    print("response data is", responseData.json())
    responsejsonData = responseData.json()
    bookingId = responsejsonData["bookingid"]
    print("Booking id is", bookingId)
    return bookingId

def test_updateData_put_req():
    token = get_token()
    bookingId = get_booking_id()

    print("token", token)
    print("booking id", bookingId)
    path_url = "/booking/" + str(bookingId)
    full_url = base_url+path_url
    cookie = "token=" + token

    headers = {
        "Content-Type" : "application/json",
        "Cookie" : cookie
    }

    payload = {
        "firstname": "Shivam",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    responseData = requests.put(url=full_url, headers=headers, json=payload)
    assert responseData.status_code == 200
    jsonResponseData = responseData.json()
    print(jsonResponseData)
    fname = jsonResponseData["firstname"]
    print(fname)
    assert jsonResponseData["firstname"] == "Shivam"


def test_delete_booking():
    fullURL = base_url + "/booking/" + str(get_booking_id())
    print(fullURL)

    headers = {
        "Content-Type" : "application/json",
        "Cookie" : "token=" + get_token()
    }

    responseData = requests.delete(url=fullURL, headers=headers)

    assert responseData.status_code == 201
