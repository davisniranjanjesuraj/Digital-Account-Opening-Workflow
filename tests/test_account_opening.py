from pages.landing_page import LandingPage
from pages.personal_details_page import PersonalDetailsPage
from pages.kyc_page import KYCPage
from pages.document_upload_page import DocumentUploadPage
from utils.test_data import VALID_USER

def test_successful_account_opening(page):
    page.goto("http://localhost:3000")

    LandingPage(page).start_account_opening()

    PersonalDetailsPage(page).enter_personal_details(
        VALID_USER["name"],
        VALID_USER["dob"],
        VALID_USER["email"]
    )

    KYCPage(page).submit_kyc(
        VALID_USER["aadhar"],
        VALID_USER["pan"]
    )

    DocumentUploadPage(page).upload_documents(
        "pan",
        VALID_USER["id_doc"],
        "utility",
        VALID_USER["address_doc"]
    )

    page.wait_for_selector("#success")
