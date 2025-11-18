from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_webtables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    # driver.maximize_window()
    # Xpath to get row elements - "//table[@id='customers']/tbody/tr"
    row_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")
    t_row = len(row_elements)
    print("Total Rows", t_row)

    # Xpath to get col elements - "//table[@id='customers']/tbody/tr[2]/td"
    col_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[2]/td")
    t_col = len(col_elements)
    print("Total columns", t_col)

    # Xpath to get the value 'Adobe' - //table[@id='customers']/tbody/tr[6]/td[1]
    # Xpath to get the value 'Italy' - //table[@id='customers']/tbody/tr[7]/td[3]

    # //table[@id='customers']/tbody/tr[ - till here it is Static
    # 7 - dynamic, row value can change from 2-7 so i(2,7)
    # ]/td[ - static
    # 3 - dynamic, col value can change from 1-3 so j(1,3)
    # ]

    first_part = "//table[@id='customers']/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2, t_row+1):
        for j in range(1, t_col+1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            print(dynamic_path, end= " ")
            data = driver.find_element(By.XPATH, dynamic_path).text
            print(data)
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country = driver.find_element(By.XPATH, country_path).text
                print(country)


