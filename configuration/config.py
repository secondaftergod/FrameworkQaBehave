from selenium import webdriver
from behave import fixture

def Browser():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH, options=options)
    return driver


class TestData:
    BROWSER = 'chrome'
    CHROME_EXECUTABLE_PATH = "drivers/chromedriver_mac"

    URL = "https://www.saucedemo.com/"
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"

    IMPLICIT_WAIT = 4
    EXPLICIT_WAIT = 10
