from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME = (By.ID,"user-name")
    PASSWORD = (By.ID,"password")
    LOGIN_BUTTON = (By.ID,"login-button")
    LOGIN_ERROR = (By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
    PRODUCTS_TITLE=(By.XPATH,"//*[@class='title']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_login(self, user, pwd):
        self.input_element(self.USERNAME, user)
        self.input_element(self.PASSWORD, pwd)

    def enter_username(self,user):
        self.input_element(self.USERNAME, user)

    def enter_password(self, pwd):
        self.input_element(self.PASSWORD, pwd)

    def enter_loginButton(self):
        self.click_element(self.LOGIN_BUTTON)

    def getTitleLogin(self):
        assert self.get_title() == "Swag Labs"

    def getTitleAfterLogin(self):
        assert self.get_element_text(self.PRODUCTS_TITLE)=="PRODUCTS"

    def invalidLogin(self):
        assert self.get_element_text(self.LOGIN_ERROR) == "Epic sadface: Username and password do not match any user in this service"

    def EmptyUsername(self):
        assert self.get_element_text(self.LOGIN_ERROR) == "Epic sadface: Username is required"

    def EmptyPassword(self):
        assert self.get_element_text(self.LOGIN_ERROR) == "Epic sadface: Password is required"