# verify negative TC - Launch VWO login page, provide invalid creds and check the error message
import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

@allure.title("Automation TCs")
@allure.description("verify negative TC - Launch VWO login page, provide invalid creds and check the error message")
@pytest.mark.negativevwologin
def test_chrome_vwo():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))

    time.sleep(7)

    usr = driver.find_element(By.ID, "login-username")
    usr.send_keys(os.getenv("INVALID_USERNAME1"))

    pass1 = driver.find_element(By.NAME, "password")
    pass1.send_keys(os.getenv("INVALID_PASSWORD"))

    submit = driver.find_element(By.ID, "js-login-btn")
    submit.click()

    time.sleep(3)

    errMsg = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(errMsg.text)

    assert errMsg.text == os.getenv("ERRORMSG")

    time.sleep(4)

    driver.quit()