import allure
import pytest
from selenium.webdriver.common.keys import Keys

from product.pages.init_app import InitAppPages


@pytest.mark.ui
@pytest.mark.positive
@pytest.mark.usefixtures("setup")
class TestCheckSearch:
    @allure.epic("Wildberries Trainee")
    @allure.title("Check search functionality")
    @allure.testcase("http://example.com/", "AM-3. Search functionality")
    @allure.description("Open home page, type text to search field, check that search result is not None")
    @allure.severity(severity_level="NORMAL")
    def test_check_search(self, config):
        expected_brand = "Nike"
        app = InitAppPages(self.driver)
        app.home_page.open_page(config)
        app.home_page.check_home_page_opened(config)
        app.navigate_bar.type_text_to_search(expected_brand)
        app.navigate_bar.type_text_to_search(Keys.ENTER)
        search_result = app.catalog_page.get_search_results()
        first_search_element = search_result[0].wrapped_element
        actual_brand = first_search_element.text
        assert search_result is not None and expected_brand in actual_brand, \
            f"The search result must contain at least one element and contains expected brand: {expected_brand}"
