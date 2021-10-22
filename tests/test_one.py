import allure
import pytest

from product.pages.us.wildberries.ru.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestOne:

    @allure.testcase("Check that home page is opened")
    @allure.description("Open home page and check that url as in config file")
    def test_open_home_page(self, config):
        home_page = HomePage(self.driver)
        home_page.open_page(config)
        home_page.click_agree_button()
        home_page.check_home_page_opened(config)
        home_page.click_burger_menu()
        home_page.choose_product_category("For women")
        home_page.choose_product_category("Clothes")
        assert "Clothes" == self.driver.title