import allure
import pytest

from product.pages.init_page import InitAppPages


@pytest.mark.usefixtures("setup")
class TestAddProductToCart:
    @allure.epic("Wildberries Trainee")
    @allure.title("Add product to cart")
    @allure.description("Open home page, type text to search field, open first search result, "
                        "check that brand as expected")
    @allure.severity(severity_level="MINOR")
    def test_add_product_to_cart(self, config):
        app = InitAppPages(self.driver)
        expected_product_name = "Nike"

        app.home_page.open_page(config)
        app.navigate_bar.type_text_to_search(expected_product_name)
        app.navigate_bar.type_text_to_search("\n")
        app.catalog_page.click_to_search_result_by_number_of_search(app.catalog_page.get_search_results(), 0)
        app.product_page.select_size(11)
        app.product_page.add_to_cart()
        app.product_page.check_confirm_message()
        app.navigate_bar.click_cart()
        items = app.product_page.get_basket_items()
        assert len(items) is not 0
