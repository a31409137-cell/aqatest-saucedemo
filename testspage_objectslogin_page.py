from playwright.sync_api import Page, Locator

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field: Locator = page.locator("#user-name")
        self.password_field: Locator = page.locator("#password")
        self.login_button: Locator = page.locator("#login-button")
        self.error_message: Locator = page.locator("[data-test='error']")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def get_error_text(self) -> str:
        return self.error_message.text_content().strip()