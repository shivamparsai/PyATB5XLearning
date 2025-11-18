import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_jsAlert():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#-------------------------------------------------------------------------#
                # Normal js alert
# -------------------------------------------------------------------------#

    normalAlert = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    normalAlert.click()

    # WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())
    time.sleep(3)

    alert = driver.switch_to.alert
    alert.accept()

    result = driver.find_element(By.ID, "result").text

    assert result == "You successfully clicked an alert"

# -------------------------------------------------------------------------#
                # confirm js alert
# -------------------------------------------------------------------------#

    confirmAlert = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    confirmAlert.click()

    # WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())
    time.sleep(3)

    alert1 = driver.switch_to.alert
    alert1.dismiss()

    result1 = driver.find_element(By.ID, "result").text
    assert result1 == "You clicked: Cancel"

# -------------------------------------------------------------------------#
                # confirm js alert
# -------------------------------------------------------------------------#

    promptAlert = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    promptAlert.click()

    # WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())
    time.sleep(3)

    alert3 = driver.switch_to.alert
    alert3.send_keys("test alert")
    alert3.accept()

    result2 = driver.find_element(By.ID, "result").text
    assert result2 == "You entered: test alert"

    print("all pass")


