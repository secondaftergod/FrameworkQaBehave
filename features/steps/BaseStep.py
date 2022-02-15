from behave import *
from pages.BuyPage import BuyPage
from pages.CheckoutPage import CheckoutPage
from pages.LoginPage import LoginPage
from pages.OverviewPage import OverviewPage
from pages.ProductPage import ProductPage
from configuration.config import Browser,TestData

@given(u'Launch the browsers')
def launch_browser(context):
    if TestData.BROWSER == 'chrome':
        context.driver = Browser()
        context.loginPage = LoginPage(context.driver)
        context.productPage = ProductPage(context.driver)
        context.buyPage = BuyPage(context.driver)
        context.checkoutPage = CheckoutPage(context.driver)
        context.overviewPage = OverviewPage(context.driver)
    else:
        raise ValueError('Browser is not supported')