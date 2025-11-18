import allure
import pytest
from selenium import webdriver

# close() - Closes the current window.
# quit() - Quits the driver and closes every associated window.

def test_vwo_on_multiple_browser_parallely_FF():
    driver = webdriver.Firefox()
    driver.get("http://katalon-demo-cura.herokuapp.com")
    driver.close()
    driver.quit()