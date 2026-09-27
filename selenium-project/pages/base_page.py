from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class containing common helper methods for all pages"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        """Navigate to a given URL"""
        self.driver.get(url)

    def find_element(self, locator):
        """Wait for an element to be visible and return it"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Wait for an element to be clickable and click it"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        """Clear the input field and type the text"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get the text of an element"""
        return self.find_element(locator).text

    def is_displayed(self, locator):
        """Check if an element is visible on the page"""
        try:
            return self.find_element(locator).is_displayed()
        except Exception:
            return False
