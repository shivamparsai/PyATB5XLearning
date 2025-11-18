import allure
import pytest
from selenium import webdriver

# To run normally, browser will open one by one
    # cmd - pytest JAN/ex02_Selenium_Basics/test05_run_on_multiple_browser_parallely.py -s
# To run parallely, all the browser will open at same time
    # we need to install one module - pip install pytest-xdist
    # cmd - pytest JAN/ex02_Selenium_Basics/test05_run_on_multiple_browser_parallely.py -n auto -s


def test_vwo_on_multiple_browser_parallely_chrome():
    driver = webdriver.Chrome()
    driver.get("http://katalon-demo-cura.herokuapp.com")

    driver.quit()

def test_vwo_on_multiple_browser_parallely_edge():
    driver = webdriver.Edge()
    driver.get("http://katalon-demo-cura.herokuapp.com")

    driver.quit()

def test_vwo_on_multiple_browser_parallely_FF():
    driver = webdriver.Firefox()
    driver.get("http://katalon-demo-cura.herokuapp.com")

    driver.quit()