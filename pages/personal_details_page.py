from pages.base_page import BasePage

class PersonalDetailsPage(BasePage):
    NAME = "#name"
    DOB = "#dob"
    EMAIL = "#email"
    CONTINUE = "#continue-kyc"

    def enter_personal_details(self, name, dob, email):
        self.fill(self.NAME, name)
        self.fill(self.DOB, dob)
        self.fill(self.EMAIL, email)
        self.click(self.CONTINUE)
