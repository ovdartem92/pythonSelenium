import allure
import pytest

from product.pages.init_app import InitAppPages


@pytest.mark.smoke
@pytest.mark.usefixtures("setup")
class TestOpenFirstSearchResult:
    @allure.epic("Wildberries Trainee")
    @allure.title("Open first search result and check product brand")
    @allure.description("Open home page, type text to search field, open first search result, "
                        "check that brand as expected")
    @allure.severity(severity_level="MINOR")
    def test_open_first_search_result_and_check_brand(self, config):
        app = InitAppPages(self.driver)
        expected_product_name = "Nike"
        app.home_page.open_page(config)
        app.navigate_bar.type_text_to_search(expected_product_name)
        app.navigate_bar.type_text_to_search("\n")
        search_result = app.catalog_page.get_search_results()
        app.catalog_page.click_to_search_result_by_number_of_search(search_result, 0)
        actual_product_name = app.product_page.get_product_brand()
        assert expected_product_name == actual_product_name
