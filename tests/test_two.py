import allure
import pytest

from product.pages.us.wildberries.ru.home_page import HomePage
from product.pages.us.wildberries.ru.catalog_page import CatalogPage


@pytest.mark.usefixtures("setup", "website_setup")
class TestTwo:

    @allure.testcase("Check search functionality")
    @allure.description("Open home page and check that url as in config file")
    def test_check_search(self, config):
        home_page = HomePage(self.driver)
        catalog_page = CatalogPage(self.driver)
        home_page.open_page(config)
        home_page.click_agree_button()
        home_page.check_home_page_opened(config)
        home_page.click_burger_menu()
        home_page.choose_product_category("For women")
        home_page.choose_product_category("Clothes")
        home_page.type_text_to_search("Nike")
        home_page.type_text_to_search("\n")
        search_result = catalog_page.get_search_results()
        assert search_result is not None
