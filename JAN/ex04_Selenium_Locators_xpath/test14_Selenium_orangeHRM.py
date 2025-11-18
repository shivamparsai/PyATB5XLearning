from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import allure
import pytest
import time

def test_orangehrm():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    usrnm = driver.find_element(By.XPATH, "//input[@name='username']")
    usrnm.send_keys("Admin")
    passw = driver.find_element(By.XPATH, "//input[@name='password']")
    passw.send_keys("admin123")
    sbmt = driver.find_element(By.XPATH, "//button[@type='submit']")
    sbmt.click()

    time.sleep(3)