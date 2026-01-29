from pages.base_page import BasePage

class DocumentUploadPage(BasePage):
    ID_TYPE = "#idType"
    ADDRESS_TYPE = "#addressType"
    ID_UPLOAD = "#idUpload"
    ADDRESS_UPLOAD = "#addressUpload"
    SUBMIT = "#submit"

    def upload_documents(self, id_type, id_file, address_type, address_file):
        self.select(self.ID_TYPE, id_type)
        self.upload_file(self.ID_UPLOAD, id_file)

        self.select(self.ADDRESS_TYPE, address_type)
        self.upload_file(self.ADDRESS_UPLOAD, address_file)

        self.click(self.SUBMIT)
