from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


def test_waits_vwo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")

    # implicit wait, this is very rarely used
    # driver.implicitly_wait(5)

    # time.sleep(5), here python Interpreter will wait for 5 sec but no the webdriver
    # for webdriver to wait we need to use implicit or explicit wait that will work on the web elements

    usrnm = driver.find_element(By.XPATH, "//input[@id='login-username']")
    usrnm.send_keys("admin")
    pass1 = driver.find_element(By.XPATH, "//input[@id='login-password']")
    pass1.send_keys("admin")
    sbmt = driver.find_element(By.XPATH, "//span[contains(text(), 'Sign in')]")
    sbmt.click()

    # Explicit wait
    WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.CLASS_NAME,"notification-box-description")))

    # Fluent wait, advance ver of explicit wait
    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    WebDriverWait(driver=driver, poll_frequency=1, timeout=5, ignored_exceptions=ignore_list).until(EC.visibility_of_element_located((By.CLASS_NAME, "notification-box-description")))

    err = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(err.text)
    assert err.text == "Your email, password, IP address or location did not match"




