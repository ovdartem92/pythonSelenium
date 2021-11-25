import allure
import pytest
from selenium.webdriver.common.keys import Keys

from product.pages.init_app import InitAppPages


@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.usefixtures("setup")
class TestOpenFirstSearchResult:
    @allure.epic("Wildberries Trainee")
    @allure.title("Check product brand in the first search result")
    @allure.testcase("http://example.com/", "AM-6. Check product brand in the first search result")
    @allure.description("Open home page, type text to search field, open first search result, "
                        "check that brand as expected")
    @allure.severity(severity_level="MINOR")
    def test_open_first_search_result_and_check_brand(self, config):
        expected_product_brand = "Nike"
        app = InitAppPages(self.driver)
        app.home_page.open_page(config)
        app.navigate_bar.type_text_to_search(expected_product_brand)
        app.navigate_bar.type_text_to_search(Keys.ENTER)
        search_result = app.catalog_page.get_search_results()
        app.catalog_page.click_to_search_result_by_number_of_search(search_result, 0)
        actual_product_brand = app.product_page.get_product_brand()
        assert expected_product_brand != actual_product_brand, \
            f"Product name shouldn't be the same." \
            f"Expected product name is {expected_product_brand}, actual product name is {actual_product_brand}"
