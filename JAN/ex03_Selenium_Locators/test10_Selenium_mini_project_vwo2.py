import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
import time

@allure.title("Automation TCs 2")
@allure.description("click on the free trial hyperlink")
@pytest.mark.positive
def test_chrome_vwo_free_trial():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))
    time.sleep(5)
#   LINK_TEXT - Exact Match
    link = driver.find_element(By.LINK_TEXT, "Start a free trial")
#   PARTIAL_LINK_TEXT - matches some part of the text
#     link = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    link.click()

    time.sleep(5)

    print(driver.current_url)

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    driver.quit()