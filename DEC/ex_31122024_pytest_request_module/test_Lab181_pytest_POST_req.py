#  POST Request (Requests) - API Automation
# - URL - https://restful-booker.herokuapp.com/booking
# - Method - POST
# - Headers -> Content-Type : application/json
# - Payload - dict
# - Auth  -> NA
# - QP/PP -> NA

# REQ
# {
#     "firstname" : "Jim",
#     "lastname" : "Brown",
#     "totalprice" : 111,
#     "depositpaid" : true,
#     "bookingdates" : {
#         "checkin" : "2018-01-01",
#         "checkout" : "2019-01-01"
#     },
#     "additionalneeds" : "Breakfast"
# }

# RES validation
# POST Response  - API Automation
# - Verify the Status Code.
# - Booking id > 0
# - Firstname, Lastname also
# - Time

import allure
import pytest
import requests


# To make Req

@allure.title("Create booking CRUD Positive")
@allure.description("Verify the create booking")
@pytest.mark.crud
def test_TC1_create_booking_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    full_url = base_url + base_path

    #   Headers will be in Dictionary

    headers = {
        "Content-Type": "application/json"
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
    response_data = requests.post(url=full_url, headers=headers, json=payload)

# response validation
# status code = 200, booking id > 0, firstname = Jim
    assert response_data.status_code == 200

    response_data_json = response_data.json()
    bookingid = response_data_json["bookingid"]
    print(bookingid)

    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int
    fname = response_data_json["booking"]["firstname"]
    print(fname)
    assert fname == "Jim"
    assert type(fname) == str
    print(response_data_json)
    lname = response_data_json["booking"]["lastname"]
    assert lname == "Brown"
    totalPrice = response_data_json["booking"]["totalprice"]
    depositPaid = response_data_json["booking"]["depositpaid"]
    assert totalPrice == 111
    assert depositPaid == True


@allure.title("Create booking CRUD negative")
@allure.description("Invalid payload, booking not done!!!!!!")
@pytest.mark.crud
def test_TC2_create_booking_negative():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    fullURL = base_url + base_path

    headers = {
        "Content-Type": "application/json"
    }

    payload = {

    }

    resposeData = requests.post(url=fullURL, headers=headers, json=payload)
    assert resposeData.status_code == 500

    print(resposeData.text)

    assert resposeData.text == "Internal Server Error"

