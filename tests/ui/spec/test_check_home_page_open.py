import allure
import pytest

from product.pages.init_app import InitAppPages


@pytest.mark.ui
@pytest.mark.positive
@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("wait_time_setup")
class TestHomePageOpened:
    @allure.epic("Wildberries Trainee")
    @allure.title("Check that home page is opened")
    @allure.testcase("http://example.com/", "AM-2. Check that home page is opened")
    @allure.description("Open home page, check that page is opened")
    @allure.severity(severity_level="MINOR")
    def test_open_home_page(self, config):
        app = InitAppPages(self.driver)
        app.home_page.open_page(config)
        app.home_page.check_home_page_opened(config)
