import allure
import pytest

from framework.browser.driver_factory import DriverFactory
from product.pages.init_app import InitAppPages


@pytest.mark.smoke
@pytest.mark.usefixtures("setup")
class TestOpenThreeBrowsersAndCheckTitleInEachInstance:
    @allure.epic("Wildberries Trainee")
    @allure.title("Open three different browsers and check title in each instance")
    @allure.description("This test shows the possibilities of creating and working with different browsers in the test")
    @allure.severity(severity_level="MINOR")
    def test_check_title_in_different_browser(self, config):
        driver_chrome = self.driver
        driver_firefox = DriverFactory().get_driver("firefox", False)
        driver_edge = DriverFactory().get_driver("edge", False)

        app_chrome = InitAppPages(driver_chrome)
        app_firefox = InitAppPages(driver_firefox)
        app_edge = InitAppPages(driver_edge)

        app_chrome.home_page.open_page(config)
        app_firefox.home_page.open_page(config)
        app_edge.home_page.open_page(config)

        title_chrome = app_chrome.home_page.get_title()
        title_firefox = app_firefox.home_page.get_title()
        title_edge = app_edge.home_page.get_title()
        driver_firefox.quit()
        driver_edge.quit()
        assert title_firefox == title_chrome == title_edge