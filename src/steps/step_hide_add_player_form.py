from playwright.sync_api import expect
from behave import given, when, then
from pages.start_page import StartPage

@then(u'formuläret för att lägga till spelare visas')
def step_impl(context):
    # start_page sätts i "Given" steget, som finns i en annan fil
    context.start_page.form_is_visible()


@then(u'spelaren klickar på knappen "Dölj"')
def step_impl(context):
    context.page.get_by_role("button", name="Dölj").click()

@then(u'formuläret för att lägga till spelare inte visas')
def step_impl(context):
    context.start_page.form_is_not_visible()
