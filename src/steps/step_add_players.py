from playwright.sync_api import expect
from behave import given, when, then
from pages.start_page import fill_player_name, player_visible


@given(u'spelaren är på startsidan')
def step_given_start_page(context):
    context.page.goto(context.base_url)


@when(u'spelaren klickar på knappen "Lägg till spelare"')
def step_when_add_player(context):
    add_button = context.page.get_by_role("button").get_by_text("Lägg till spelare")
    add_button.click(timeout=100)


@when(u'spelaren skriver "{user1}" i textfältet')
def step_when_player_types_name(context, user1):
    fill_player_name(context.page, user1)


@then(u'"{user}" dyker upp på sidan med texten "0:00.0"')
def step_player_name_visible(context, user):
    element = player_visible(context.page, user)
    expect(element).to_be_visible(timeout=100)
