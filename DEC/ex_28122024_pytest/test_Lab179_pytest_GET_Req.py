# Request module - package or library - for API testing. it has all the HTTp methods
# like (GET, POST, PUT, DELETE, PATCH etc)
# to install req module - pip install requests
# to see the api response - --alluredir=allure_results -s
# we can install all in one time - pip install pytest allure requests

import pytest
import allure
import requests

@allure.title("Verify the GET req/res of restful booker positive")
@allure.description("This is to check the booking 1 and verify the response")
@pytest.mark.positive
def test_get_req_positive():
    URL = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url=URL)
    print(responseData.text)
    assert responseData.status_code == 200

# or like below (but not recommended)

# def test_get_req_positive():
#     assert requests.get("https://restful-booker.herokuapp.com/booking/1").status_code == 200

@allure.title("Verify the GET req/res of restful booker negative")
@allure.description("This is to check the booking -1 and verify the response for invalid case")
@pytest.mark.negative
def test_get_req_negative():
    URL1 = "https://restful-booker.herokuapp.com/booking/-1"
    resData = requests.get(url=URL1)
    assert  resData.status_code == 200
