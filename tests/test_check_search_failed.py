import allure
import pytest

from product.pages.init_app import InitAppPages


@pytest.mark.smoke
@pytest.mark.usefixtures("setup", "website_setup")
class TestCheckSearch:
    @allure.epic("Wildberries Trainee")
    @allure.title("Check search functionality")
    @allure.testcase("https://goldcast.atlassian.net/browse/AM-467",
                     "Search functionality")
    @allure.description("Open home page, type text to search field, check that search result is not None")
    @allure.severity(severity_level="NORMAL")
    def test_check_search(self, config):
        app = InitAppPages(self.driver)
        app.home_page.open_page(config)
        app.home_page.check_home_page_opened(config)
        app.navigate_bar.type_text_to_search("Nike")
        app.navigate_bar.type_text_to_search("\n")
        search_result = app.catalog_page.get_search_results()
        assert search_result is None
