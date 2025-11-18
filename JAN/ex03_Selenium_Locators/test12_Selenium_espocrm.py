from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
import time
import allure
import pytest

def test_espocrm_page():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(4)
    login_btn = driver.find_element(By.XPATH, "//button[@id='btn-login']")
    # login_btn = driver.find_element(By.XPATH, "//div[text()='Login']")
    # login_btn = driver.find_element(By.ID, "btn-login")
    login_btn.click()

    # h_link = driver.find_element(By.LINK_TEXT, "Advanced Pack")
    # h_link.click()

    time.sleep(5)

    driver.quit()
