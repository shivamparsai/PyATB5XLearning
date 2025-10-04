# You can use the fixture in context to the test.
# Similar - pre condition, post condition.


import pytest

@pytest.fixture()
def is_Married():
    return True

def test_update(is_Married):
    assert is_Married == True