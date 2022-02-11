from behave import *
from configuration.config import Browser,TestData
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage

@given(u'Launch the browsers')
def launch_browser(context):
    if TestData.BROWSER == 'chrome':
        context.driver = Browser()
    else:
        raise ValueError('Browser is not supported')

@when(u'Open the "https://www.saucedemo.com/" website and login whith username "{user}" and password "{pwd}"')
def open_login_page(context,user,pwd):
    try:
        context.driver.get(TestData.URL)
        context.loginPage = LoginPage(context.driver)
        context.loginPage.enter_login(user, pwd)
        context.productPage=ProductPage(context.driver)
    except:
        context.driver.close()
        assert False,"Test is failed in open login page or login"
@then(u'The product page open')
def checkProductPage(context):
    try:
        context.productPage.checkProduct_page()
    except:
        context.driver.close()
        assert False, "Test is failed in validate product page title"
@then(u'Add items to card')
def addItemsToBasket(context):
    try:
        context.productPage.addItemsToCard()
    except:
        context.driver.close()
        assert False, "Test is failed when add all items to card"
@then(u'Check items in basket')
def checkBasket(context):
    try:
        context.productPage.checkAddItemsInBasket()
    except:
        context.driver.close()
        assert False, "Test items after add in basket failed"

