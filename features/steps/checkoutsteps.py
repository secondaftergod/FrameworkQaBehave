from behave import *

@then(u'Click on the checkout button')
def step_impl(context):
   context.buyPage.goToCheckout()

@then(u'Check title checkout page')
def step_impl(context):
   try:
      context.checkoutPage.check_page()
   except:
      assert False,'Failed on go to page'

