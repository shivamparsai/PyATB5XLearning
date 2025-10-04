import pytest

@pytest.fixture()
def get_token():
    return "abc"

@pytest.fixture()
def get_booking_id():
    return 1

def test_update_data(get_token, get_booking_id)
    print(get_token)
    print(get_booking_id)