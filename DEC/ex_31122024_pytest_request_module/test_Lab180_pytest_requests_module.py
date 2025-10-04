# To run the Tcs if they have marked - cmd - ex - `pytest -m "smoke" src/Oct/test_Lab176.py`

import requests
import allure
import pytest

@allure.title("TC1 - Verify that 2+2 == 4")
@allure.description("This is a basic math test addition")
@pytest.mark.smoke
def test_add():
    assert 2+2 == 4

@allure.title("TC2 - Verify that 3-3 == 0")
@allure.title("This is a basic math test sub")
@pytest.mark.regression
def test_sub():
    assert 3-3 == 0

@allure.title("TC3 - Verify that 1*1 == 1")
@allure.description("This is a basic math test mul")
@pytest.mark.smoke
def test_mul():
    assert  1*1 == 1

# below TCs will always be skipped from execution because we have marked as skip
@pytest.mark.skip(reason="not working now, skip it from execution")
def test_div():
    assert 1/0 == 0