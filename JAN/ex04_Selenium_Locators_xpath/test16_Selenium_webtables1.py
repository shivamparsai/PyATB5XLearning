from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_webtables1():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")
    driver.maximize_window()
    table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody")
    row_t = table.find_elements(By.TAG_NAME, "tr")

    # or

    # row_t = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody/tr[1]/td")

    for row in row_t:
        cols = row.find_elements(By.TAG_NAME, "td")
        for e in cols:
            print(e.text)


