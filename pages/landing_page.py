from pages.base_page import BasePage

class LandingPage(BasePage):
    START_BUTTON = "#start-account"

    def start_account_opening(self):
        self.click(self.START_BUTTON)
