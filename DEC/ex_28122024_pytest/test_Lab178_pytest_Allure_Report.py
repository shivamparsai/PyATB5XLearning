# install allure report - pip install allure-pytest
# need to add the below while running the pytest TCs
# --alluredir=<folder name> ex- --alluredir=allure_results, to run this cmd we should have node js
# ex- pytest DEC/ex_28122024_pytest/test_Lab178_pytest_Allure_Report.py --alluredir=allure_results
# also install allure commandline through cmd prompt - npm -g i allure-commandline
# cmd to see the report - allure serve <folder name> ex- allure serve allure_results

import pytest
import allure       # to use more functions from Allure

@allure.title("Positive TCs Results")
@allure.description("This TC is running and providing the Positive result")

@pytest.mark.positive
def test_method_positive():
    print("This is positive TC")
    assert 1+1 == 2

@allure.title("Negative TCs Results")
@allure.description("This TC is running and providing the Negative result")

@pytest.mark.negative
def test_method_negative():
    print("This is negative TC")
    assert 2-2 == 2