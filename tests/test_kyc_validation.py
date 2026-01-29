def test_invalid_kyc_rejection(page):
    page.goto("http://localhost:3000")

    from pages.kyc_page import KYCPage
    from utils.test_data import INVALID_KYC

    KYCPage(page).submit_kyc(
        INVALID_KYC["aadhar"],
        INVALID_KYC["pan"]
    )

    assert "KYC Failed" in page.content()
