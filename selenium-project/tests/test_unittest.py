import unittest
from utils import get_driver
from pages.login_page import LoginPage
from pages.search_page import SearchPage

class TestECommerceUnittest(unittest.TestCase):
    """Test Suite demonstrating Unittest with Page Object Model"""

    def setUp(self):
        """Runs before every test: starts the browser"""
        self.driver = get_driver()

    def tearDown(self):
        """Runs after every test: closes the browser"""
        if self.driver:
            self.driver.quit()

    def test_invalid_login(self):
        """Verify invalid login displays error banner"""
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login("invalid_unittest_user@test.com", "wrong_password_123")

        self.assertTrue(login_page.is_warning_displayed())
        self.assertIn("Warning", login_page.get_warning_message())

    def test_search_product(self):
        """Verify searching for a valid product returns results"""
        search_page = SearchPage(self.driver)
        search_page.open()
        search_page.search_product("MacBook")

        results = search_page.get_product_results()
        self.assertGreater(len(results), 0, "Expected at least 1 product in search results")

if __name__ == "__main__":
    unittest.main()
