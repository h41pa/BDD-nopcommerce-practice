from behave import *

@given('I am on the Add/Remove Elements')
def step_impl(context):
    context.add_remove.navigate_page()


@when('I Add Element')
def step_impl(context):
    context.add_remove.add_elem()

@when('I Remove Element')
def step_impl(context):
    context.add_remove.delete_element()


