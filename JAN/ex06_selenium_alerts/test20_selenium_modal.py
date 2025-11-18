import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_modal():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://lithohtml.themezaa.com/modal-simple.html")
    modalOpen = driver.find_element(By.XPATH, "//a[text()='Open Modal']")
    modalOpen.click()

    WebDriverWait(driver=driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, "//button[@title='Close (Esc)']")))

    closeModal = driver.find_element(By.XPATH, "//button[@title='Close (Esc)']")
    closeModal.click()

    time.sleep(2)