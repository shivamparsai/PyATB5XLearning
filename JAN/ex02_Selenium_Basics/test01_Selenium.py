# to install selenium - pip install selenium
# when we install selenium 4, it will automatically install the selenium-manager also
# which will have all the drivers of the browsers itself.

import time

import allure
import pytest
from selenium import webdriver


@allure.title("1st selenium script")
def test_vwo_home():
    driver = webdriver.Chrome()
    driver.get("http://app.vwo.com")
    print(driver.session_id)
    time.sleep(20)

    driver.quit()