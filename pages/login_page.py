from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import get_config

class LoginPage(BasePage):
    """Page Object for the Login Page"""

    # Locators
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")
    WARNING_ALERT = (By.CSS_SELECTOR, ".alert-danger")

    def open(self):
        """Open the login page directly"""
        base_url = get_config("base_url")
        self.open_url(f"{base_url}index.php?route=account/login")

    def login(self, email, password):
        """Enter credentials and click login button"""
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_warning_message(self):
        """Return the warning error message text"""
        return self.get_text(self.WARNING_ALERT)

    def is_warning_displayed(self):
        """Check if warning alert is visible"""
        return self.is_displayed(self.WARNING_ALERT)
