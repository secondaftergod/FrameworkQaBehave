from behave import *


@then(u'Click on buy button')
def step_impl(context):
    context.productPage.clickOnBuyButton()

@then(u'Check title')
def step_impl(context):
    try:
        context.buyPage.check_page()
    except:
        context.driver.close()
        assert False,'Failed go on BuyPage'

@then(u'Check items inside buy page')
def step_impl(context):
    try:
        context.buyPage.check_itemsOnPage()
    except:
        context.driver.close()
        assert False,'Not all items on BuyPage'

@then(u'Remove all items from buyPage')
def step_impl(context):
    try:
        context.buyPage.removeItems()
    except:
        context.driver.close()
        assert True,'Items not deleted'


