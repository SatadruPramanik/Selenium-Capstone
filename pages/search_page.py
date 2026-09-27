from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import get_config

class SearchPage(BasePage):
    """Page Object for the Search Functionality"""

    # Locators
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")
    PRODUCT_TITLES = (By.CSS_SELECTOR, ".product-layout .caption h4 a")
    NO_PRODUCT_MESSAGE = (By.XPATH, "//p[contains(text(),'There is no product that matches the search criteria.')]")

    def open(self):
        """Open the Home / Search page directly"""
        base_url = get_config("base_url")
        self.open_url(base_url)

    def search_product(self, product_name):
        """Enter product name and click search"""
        self.enter_text(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def get_product_results(self):
        """Return list of product titles shown in search results"""
        elements = self.driver.find_elements(*self.PRODUCT_TITLES)
        return [el.text for el in elements if el.text]

    def is_no_product_message_displayed(self):
        """Check if 'no product found' message is visible"""
        return self.is_displayed(self.NO_PRODUCT_MESSAGE)
