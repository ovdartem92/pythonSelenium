import allure
import pytest

from product.pages.init_app import InitAppPages


@pytest.mark.ui
@pytest.mark.positive
@pytest.mark.usefixtures("setup")
class TestChooseProductCategory:
    @allure.epic("Wildberries Trainee")
    @allure.title("Check that user can enter to Clothes product category")
    @allure.testcase("http://example.com/", "AM-5. Check that user can enter to Clothes product category")
    @allure.description("Open home page, choose product category to For Women > Clothes, "
                        "check that the title on page is Clothes")
    @allure.severity(severity_level="CRITICAL")
    def test_choose_product_category(self, config):
        app = InitAppPages(self.driver)
        expected_product_category = "Clothes"
        app.home_page.open_page(config)
        app.home_page.check_home_page_opened(config)
        app.navigate_bar.click_burger_menu()
        app.home_page.choose_product_category("For women")
        app.home_page.choose_product_category(expected_product_category)
        actual_product_category = self.driver.title
        assert expected_product_category == actual_product_category, \
            f"Expected product category is {expected_product_category}, actual product category is {actual_product_category}"
