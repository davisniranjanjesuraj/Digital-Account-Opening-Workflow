from pages.base_page import BasePage

class KYCPage(BasePage):
    AADHAR = "#aadhar"
    PAN = "#pan"
    CONTINUE = "#continue-docs"

    def submit_kyc(self, aadhar, pan):
        self.fill(self.AADHAR, aadhar)
        self.fill(self.PAN, pan)
        self.click(self.CONTINUE)
