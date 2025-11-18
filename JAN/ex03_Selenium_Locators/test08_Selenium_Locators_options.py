import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_browser_options():

    chrome_options = Options()

    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--window-size=800,500")
    chrome_options.add_argument("--headless")   # means No UI

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    e = driver.find_element(By.ID, "btn-make-appointment")
    e.click()

    time.sleep(5)

    driver.quit()
