import re

from behave import given, when, then

@given(u'spelaren är på startsidan')
def step_given_start_page(context):
    context.page.goto(context.base_url)


@when(u'spelaren klickar på knappen "Lägg till spelare"')
def step_when_add_player(context):
    add_button = context.page.get_by_role("button").get_by_text("Lägg till spelare")
    add_button.click(timeout=100)

def fill_player_name(page, name):
    page.get_by_role("textbox").fill(name)

@when(u'spelaren skriver "David" i textfältet')
def step_impl(context):
    #context.page.get_by_role("textbox").fill("David")
    fill_player_name(context.page, "David")


@then(u'"David" dyker upp på sidan med texten "0:00.0"')
def step_impl(context):
    context.page.get_by_text(re.compile("David\s+0:00.0"))


@when(u'spelaren skriver "Gerson" i textfältet')
def step_impl(context):
    fill_player_name(context.page, "Gerson")


@then(u'"Gerson" dyker upp på sidan med texten "0:00.0"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then "Gerson" dyker upp på sidan med texten "0:00.0"')
