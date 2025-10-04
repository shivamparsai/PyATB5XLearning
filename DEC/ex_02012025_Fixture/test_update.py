import allure
import requests
import pytest

def test_update_data(get_token, get_booking_id):
    token = get_token
    booking_id = get_booking_id

    print(token)
    print(booking_id)