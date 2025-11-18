import time

from selenium import webdriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.actions.mouse_button import MouseButton


def test_mouseAction():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    click = driver.find_element(By.ID, "click")
    click.click()
    time.sleep(3)
    actions = ActionBuilder(driver=driver)
    actions.pointer_action.pointer_up(MouseButton.BACK)
    actions.perform()
    time.sleep(3)
    
    
    holdElement = driver.find_element(By.ID, "draggable")
    actions1 = ActionChains(driver)
    actions1.click_and_hold(on_element=holdElement).perform()
    time.sleep(3)

    
    driver.quit()