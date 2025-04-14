import re
from playwright.sync_api import expect


class StartPage:
    def __init__(self, page):
        self.page = page


    # Gemensamma funktioner
    def fill_player_name(self, name):
        self.page.get_by_role("textbox").fill(name)

    def player_visible(self, name):
        return self.page.locator(".player").get_by_text(re.compile(name + "\s+0:00.0"))


    def form_is_visible(self):
        # 1 hämta label, input och button
        # 2 kontrollera att alla syns
        name_regex = re.compile("Nya spelarens namn")

        label = self.page.get_by_text(name_regex)
        # obs lägg till "ignore case" till regex
        expect(label).to_be_visible(timeout=100)

        input_text = self.page.get_by_label(name_regex)
        expect(input_text).to_be_visible(timeout=100)

        button = self.get_button__add_player()
        expect(button).to_be_visible(timeout=100)

    def form_is_not_visible(self):
        name_regex = re.compile("Nya spelarens namn")

        label = self.page.get_by_text(name_regex)
        # obs lägg till "ignore case" till regex
        expect(label).not_to_be_visible(timeout=100)

        input_text = self.page.get_by_label(name_regex)
        expect(input_text).not_to_be_visible(timeout=100)


    def get_button__add_player(self):
        return self.page.get_by_role("button").get_by_text("Lägg till spelare")

