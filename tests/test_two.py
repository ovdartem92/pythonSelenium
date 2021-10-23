import allure
import pytest

from product.pages.us.wildberries.ru.catalog_page import CatalogPage
from product.pages.us.wildberries.ru.home_page import HomePage


@pytest.mark.usefixtures("setup", "website_setup")
class TestTwo:
    @allure.epic("Wildberries Trainee")
    @allure.title("Check search functionality")
    @allure.testcase("https://goldcast.atlassian.net/browse/AM-467",
                     "Search functionality")
    @allure.description("Open home page, type text to search field, check that search result is not None")
    @allure.severity(severity_level="normal")
    def test_check_search(self, config):
        home_page = HomePage(self.driver)
        catalog_page = CatalogPage(self.driver)
        home_page.open_page(config)
        home_page.click_agree_button()
        home_page.check_home_page_opened(config)
        home_page.click_burger_menu()
        home_page.type_text_to_search("Nike")
        home_page.type_text_to_search("\n")
        search_result = catalog_page.get_search_results()
        assert search_result is not None
