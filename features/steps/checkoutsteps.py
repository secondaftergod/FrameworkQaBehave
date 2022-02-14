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

@then(u'Provide the firstname "{first}" and lastname "{last}" and zip "{zip}"')
def step_impl(context,first,last,zip):
    context.checkoutPage.whriteInfo(first,last,zip)

@then(u'Click on the continue button')
def step_impl(context):
    context.checkoutPAge.clickContinueButton()

@then(u'Error checkout')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Error checkout')




