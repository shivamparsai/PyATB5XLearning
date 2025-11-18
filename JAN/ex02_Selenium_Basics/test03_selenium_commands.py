import time

from selenium import webdriver
import allure
import pytest

@allure.title("Verify the title")
def test_vwo_homepage():
    driver = webdriver.Chrome()
    driver.get("http://app.vwo.com")
    print(driver.title)
    print(driver.current_url)
    print(driver.page_source)
    assert driver.title == "VWO - Application"
    time.sleep(10)

    driver.quit()