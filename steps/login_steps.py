from behave import *


# trebuie luat din login.feature pentru fiecare pass in parte
# pentru fiecare given,when.,then
# step_impl - asa se vor numi
# un step chair daca e repetat gen @given('I am on the Login Page') si clicked on login button(vezi feature)
# se defineste o singura data pentru a nu da erori si trebuie acelasi nume in toate   .
# cu parametri folosing {} gen emali message

@given('I am on the Login Page')
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when('I insert an unregistered email in the mail input')
def step_impl(context):
    context.login_page.set_email("email_neinregistrat@host.com")


@when('I insert "{email}" in the mail input')  # pentru scenariu cu paramentru
def step_impl(context, email):
    context.login_page.set_email(email)


@when('I insert a password in the password input')
def step_impl(context):
    context.login_page.set_password("password")


@when('I click on the login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('The main error message is displayed')
def step_impl(context):
    assert context.login_page.is_main_error_message_displayed(), "Error message not displayed"


@then('The error message contains "{message}" message')
def step_impl(context, message):
    assert message in context.login_page.get_main_error_message_text()


@when('I insert " " in the email input')
def step_impl(context):
    context.login_page.set_email(" ")


@then('Email error message is displayed')
def step_impl(context):
    context.login_page.is_email_error_message_displayed()


@then('Email error text contains "{message}"')
def step_impl(context, message):
    assert message in context.login_page.get_email_error_message_text()


@then('The login page URL is "{expected_url}"')
def step_impl(context, expected_url):
    assert context.login_page.is_url_correct(expected_url), f"Error, page URL is not {expected_url}"
