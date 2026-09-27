import pytest
from pages.login_page import LoginPage
from utils import read_csv

# Load test data from data/login_data.csv
login_test_data = read_csv("login_data.csv")

class TestLogin:
    """Login Test Suite using PyTest and Page Object Model"""

    @pytest.mark.parametrize("scenario,email,password,expected", login_test_data)
    def test_login_scenarios(self, driver, scenario, email, password, expected):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(email, password)

        # Verify warning message appears for invalid login
        assert login_page.is_warning_displayed(), f"Failed on scenario: {scenario}"
        assert "Warning" in login_page.get_warning_message()
