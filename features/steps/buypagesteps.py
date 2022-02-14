from behave import *


@then(u'Click on buy button')
def step_impl(context):
    context.productPage.clickOnBuyButton()

@then(u'Check title')
def step_impl(context):
    context.buyPage.check_page()

