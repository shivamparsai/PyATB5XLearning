from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions import mouse_button
import time
import allure

def testMmt():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--incognito")
    driver = webdriver.Chrome(chromeOptions)
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    # modal = driver.find_element(By.XPATH, "//span[@data-cy='closeModal']")

    WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='closeModal']"))).click()

    fromCity = driver.find_element(By.ID, "fromCity")
    fromCity.send_keys("del")

    time.sleep(2)

    actions = ActionChains(driver=driver)
    actions.move_to_element(fromCity).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()


    time.sleep(2)
