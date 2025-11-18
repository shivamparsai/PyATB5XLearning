from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import allure
import pytest

def test_vwo_home():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(4)
    loginbtn = driver.find_element(By.XPATH, "//a[text()='Make Appointment']")
    loginbtn.click()
    time.sleep(3)
    driver.quit()