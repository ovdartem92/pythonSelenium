import allure
import pytest

from product.pages.init_page import InitAppPages


@pytest.mark.usefixtures("setup")
class TestHomePageOpened:
    @allure.epic("Wildberries Trainee")
    @allure.title("Check that home page is opened")
    @allure.description("Open home page, check that page is opened")
    @allure.severity(severity_level="CRITICAL")
    def test_open_home_page(self, config):
        app = InitAppPages(self.driver)
        app.home_page.open_page(config)
        app.home_page.check_home_page_opened(config)
