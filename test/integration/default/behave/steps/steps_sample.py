# file:features/steps/steps_sample.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
from strlib import StrLib


@given('we have a string "{str_val}"')
def step_impl(context, str_val):
    context.str_lib1 = StrLib()
    context.str_val = str_val


@when('we get a string')
def step_impl(context):
    context.str_lib1.set_string()


@then('both should be equal')
def step_impl(context):
    assert context.str_lib1.returned == context.str_val


@given('we have two strings {str_val1} {str_val2}')
def step_impl(context, str_val1, str_val2):
    context.str_lib2 = StrLib()
    context.str_val1 = str_val1
    context.str_val2 = str_val2


@when('we get the strings')
def step_impl(context):
    context.str_lib2.set_two_strings()


@then('strings that we have and got are equal')
def step_impl(context):
    assert context.str_lib2.returned == (context.str_val1, context.str_val2)
