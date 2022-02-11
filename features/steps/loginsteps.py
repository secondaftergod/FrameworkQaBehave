from behave import *
from configuration.config import Browser,TestData
from pages.LoginPage import LoginPage



@given(u'Launch the browser')
def launch_browser(context):
    if TestData.BROWSER == 'chrome':
        context.driver = Browser()
    else:
        raise ValueError('Browser is not supported')


@when(u'Open the "https://www.saucedemo.com/" website')
def open_login_page(context):
    try:
        context.driver.get(TestData.URL)
        context.loginPage = LoginPage(context.driver)
    except:
        context.driver.close()
        assert False,"Test is failed in open login page"

@then(u'The login has been opened')
def validate_login_page(context):
    try:
        context.loginPage.getTitleLogin()
    except:
        context.driver.close()
        assert False, "Test is failed in validate login page title"


@then(u'Provide the username "{user}" and password "{pwd}"')
def enter_login_creds(context, user, pwd):
    try:
        context.loginPage.enter_login(user,pwd)
    except:
        context.driver.close()
        assert False, "Test is failed in enter login credentials"


@then(u'Click on the Login button')
def enter_login(context):
    try:
        context.loginPage.enter_loginButton()
    except:
        context.driver.close()
        assert False, "Test is failed in enter login"


@then(u'Login is successful and productpage is opened')
def validate_product_page(context):
    try:
        context.loginPage.getTitleAfterLogin()
    except:
        context.driver.close()
        assert False, "Test is failed in login"

@then(u'Login is failed with invlid username and password')
def invalid_login(context):
    try:
        context.loginPage.invalidLogin()
    except:
        context.driver.close()
        assert False, "Test is failed in validating invalid login"

@then(u'Provide the password "{pwd}"')
def enter_login(context, pwd):
    try:
        context.loginPage.enter_password(pwd)
    except:
        context.driver.close()
        assert False, "Test is failed in enter password"

@then(u'Provide the username "{user}"')
def enter_login(context, user):
    try:
        context.loginPage.enter_username(user)
    except:
        context.driver.close()
        assert False, "Test is failed in enter username"

@then(u'Login is failed and empty username error is displayed')
def validate_empty_username(context):
    try:
        context.loginPage.EmptyUsername()
    except:
        context.driver.close()
        assert False, "Test is failed in validate empty username"

@then(u'Login is failed and empty password error is displayed')
def validate_empty_passeword(context):
    try:
        context.loginPage.EmptyPassword()
    except:
        context.driver.close()
        assert False, "Test is failed in validate empty password"



@then(u'Close the browser')
def step_impl(context):
    context.driver.close()