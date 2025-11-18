import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest

def test_clickButton():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    e = driver.find_element(By.ID, "btn-make-appointment")
    e.click()

    time.sleep(5)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    print(driver.current_url)

    driver.quit()

