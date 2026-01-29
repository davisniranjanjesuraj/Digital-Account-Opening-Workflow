from pathlib import Path

class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, selector):
        self.page.wait_for_selector(selector, state="visible")
        self.page.click(selector)

    def fill(self, selector, value):
        self.page.wait_for_selector(selector, state="visible")
        self.page.fill(selector, value)

    def select(self, selector, value):
        self.page.wait_for_selector(selector, state="visible")
        self.page.select_option(selector, value)

    def upload_file(self, selector, file_path):
        path = Path(file_path).resolve()
        self.page.wait_for_selector(selector, state="visible")
        self.page.set_input_files(selector, str(path))
