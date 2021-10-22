import allure
import pytest

from product.pages.com.yahoo.home_page import HomePage


@pytest.mark.usefixtures("setup", "website_setup")
class Test:

    @allure.title("Open home page")
    @allure.description("Open home page and check that url as in config file")
    def test_open_home_page(self, config):
        home_page = HomePage(self.driver)
        home_page.open_home_page(config)
        home_page.click_to_logo()
        home_page.check_home_page_opened(config)
