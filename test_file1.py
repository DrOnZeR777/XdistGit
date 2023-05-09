# Pytest Framework Creation
# TestCase001
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Test_pytest():

    def test_case_001(self):  # --->Test Cases --> always strat with test_
        a = 10
        b = 20
        add = a + b
        print(add)
        if add == 30:
            print("test_case_001 is passed")
            assert True
        else:
            print("test_case_001 is failed")
            assert False

    def test_case_002(self):
        a = 10
        b = 7
        mul = a * b
        print(mul)
        if mul == 70:
            print("test_Case_002 is Passed", mul)
            assert True
        else:
            print("test_Case_002 is Failed", mul)
            assert False

    def addi_case_003(self):
        a = 10
        b = 20
        addition = a + b
        print(addition)

        if addition == 30:
            print("The Addi is Passed.... ")
            assert True
        else:
            print("The Addi is failed...")
            assert False

    def test_googl_page(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.co.in/")
        time.sleep(10)

        logo = driver.find_element(By.CLASS_NAME,"lnXdpd").is_displayed()
        print(logo)
        if logo == True:
            assert True
        else:
            assert False

        driver.close()