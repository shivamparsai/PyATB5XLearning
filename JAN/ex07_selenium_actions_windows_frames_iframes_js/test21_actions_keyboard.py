from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import allure
import time

@allure.title("Actions")
@allure.description("different actions")
def testVerifyActionKeyboard():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/practice.html")
    fname = driver.find_element(By.NAME, "firstname")
    actions = ActionChains(driver=driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(fname, "shivam").perform()
    time.sleep(4)
    driver.quit()


