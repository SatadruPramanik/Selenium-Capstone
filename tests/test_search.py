import pytest
from pages.search_page import SearchPage
from utils import read_csv

# Load test data from data/search_data.csv
search_test_data = read_csv("search_data.csv")

class TestSearch:
    """Product Search Test Suite using PyTest and Page Object Model"""

    @pytest.mark.parametrize("scenario,search_term,expected", search_test_data)
    def test_search_scenarios(self, driver, scenario, search_term, expected):
        search_page = SearchPage(driver)
        search_page.open()
        search_page.search_product(search_term)

        if expected == "found":
            products = search_page.get_product_results()
            assert len(products) > 0, f"Expected products for {search_term}"
            assert any(search_term.lower() in p.lower() for p in products)
        else:
            assert search_page.is_no_product_message_displayed()
