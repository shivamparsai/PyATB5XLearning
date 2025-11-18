# katalon-demo-cura.herokuapp.com
# python interpreter is closing the browser automatically
import time

import allure
import pytest
from selenium import webdriver

@allure.title("verify the title of vwo.com")
def test_vwo_title():
    driver = webdriver.Chrome()
    driver.get("http://katalon-demo-cura.herokuapp.com")

    if "CRA Healthcare Service" in driver.page_source:
        print("Text found")
    else:
        print("Text not found")

    # below is the pytest function to fail the TCs explicitly
        pytest.fail("Text not found")

    time.sleep(10)

    driver.quit()

