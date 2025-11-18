import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_mac_mini():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.ebay.com/")
    search = driver.find_element(By.XPATH, "//input[@title='Search']")
    search.send_keys("mac mini")
    btn = driver.find_element(By.XPATH, "//button[@id='gh-search-btn']")
    btn.click()
    time.sleep(10)

    # # e = driver.find_elements(By.XPATH, "//span[@class='su-styled-text primary default'][contains(text(), 'Apple Mac Mini')]")
    # e = driver.find_elements(By.XPATH, "(//span[@class='su-styled-text primary default'][contains(text(),'Apple Mac Mini')])")
    # total_record = len(e)
    # print(total_record)
    #
    # for i in range(0,total_record+1):
    #     if i <= 10:
    #         first_part = "(//span[@class='su-styled-text primary default'][contains(text(),'Apple Mac Mini')])["
    #         second_part = "]"
    #         final_part = f"{first_part}{i}{second_part}"
    #         # print("test", final_part)
    #         WebDriverWait(driver=driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, final_part)))
    #
    #         e1 = driver.find_element(By.XPATH, final_part).text
    #         print(e1)

    list_items = driver.find_elements(By.XPATH, "//div[@class='s-card__title']")
    list_items_prize = driver.find_elements(By.XPATH, "//span[@class='su-styled-text primary bold large-1 s-card__price']")

    titleText = [title.text for title in list_items]    # to convert web element into list
    priceText = [price.text for price in list_items_prize]  # to convert web element into list
    for title,price in zip(titleText,priceText):            # to combine 2 lists
        # for price in priceText:
        print(title,price)



    # for items in list_items:
    #     print(items.text)
    #
    # for i in list_items_prize:
    #     print(i.text)
