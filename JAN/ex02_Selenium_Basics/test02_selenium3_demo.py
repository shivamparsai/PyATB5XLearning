# in selenium 3, first we need to download browser (chrome, edge, etc) separately for testing  and
# also need to download the respective browser's server and need to give the path in the code

import allure
import pytest
from selenium import webdriver

def test_selenium3():
    driver_path = "user/shivam/Downloads/ChromeDriver"
    driver = webdriver.EdgeService(executable_path=driver_path)
    driver.get("http://app.vwo.com")

    driver.quit()