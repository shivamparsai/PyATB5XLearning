from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
import time
import allure
import pytest

@allure.title("Automation TC 3")
@allure.description("verify the number of links available on the page")
@pytest.mark.positive
def test_find_links():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))
    time.sleep(4)
    # all_links = driver.find_elements(By.TAG_NAME, "button")
    all_links = driver.find_elements(By.TAG_NAME, "a")
    print(len(all_links))
    time.sleep(4)

    for i in all_links:
        print(i.text)
        if "Start a free trial" in i.text:
            i.click()

    time.sleep(4)

    driver.quit()
