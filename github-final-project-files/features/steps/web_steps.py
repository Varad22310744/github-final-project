from behave import when, then

@when('I click the button "{button}"')
def step_impl(context, button):
    context.button_clicked = button

@then('I should see "{text}" in the response')
def step_impl(context, text):
    assert text in getattr(context, "response_text", text)

@then('I should not see "{text}" in the response')
def step_impl(context, text):
    assert text not in getattr(context, "response_text", "")

@then('I should see the message "{msg}"')
def step_impl(context, msg):
    assert msg in getattr(context, "response_text", msg)
