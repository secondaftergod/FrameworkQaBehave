from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):
    checkout_title = (By.XPATH,"//*[@id='header_container']/div[2]/span")
    cancel_button = (By.XPATH,"//*[@id='cancel']")
    order_firstName = (By.XPATH,"//*[@id='first-name']")
    order_lastName = (By.XPATH,"//*[@id='last-name']")
    order_Zip = (By.XPATH,"//*[@id='postal-code']")
    continue_button = (By.XPATH,"//*[@id='continue']")
    infoError = (By.XPATH,"//*[@data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def check_page(self):
        assert self.get_element_text(self.checkout_title)=="CHECKOUT: YOUR INFORMATION"

    def clickContinueButton(self):
        self.click_element(self.continue_button)

    def whriteInfo(self,first,last,zip):
        self.input_element(self.order_firstName,first)
        self.input_element(self.order_lastName,last)
        self.input_element(self.order_Zip,zip)

    def errorCheck(self):
        assert self.verify_element_displayed(self.infoError)==True
