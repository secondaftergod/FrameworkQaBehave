from behave import *

@then(u'Check price item and total price')
def step_impl(context):
    try:
        context.overviewPage.assert_price()
    except:
        assert False,'Price buy items and price total price item not true'
@then(u'Check eq prices')
def step_impl(context):
    try:
        context.overviewPage.eqFullprice()
    except:
        assert False, 'Price buy items+tax and price total not true'




