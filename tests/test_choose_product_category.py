import allure
import pytest

from product.pages.init_page import InitPage


@pytest.mark.usefixtures("setup")
class TestChooseProductCategory:
    @allure.epic("Wildberries Trainee")
    @allure.title("Check that user can enter to Clothes product category")
    @allure.testcase("https://goldcast.atlassian.net/browse/AM-468",
                     "Change product category")
    @allure.description("Open home page, choose product category to For Women > Clothes, "
                        "check that the title on page is Clothes")
    @allure.severity(severity_level="CRITICAL")
    def test_choose_product_category(self, config):
        app = InitPage(self.driver)
        expected_product_category = "Clothes"
        app.home_page.open_page(config)
        app.home_page.click_agree_button()
        app.home_page.check_home_page_opened(config)
        app.navigate_bar.click_burger_menu()
        app.home_page.choose_product_category("For women")
        app.home_page.choose_product_category(expected_product_category)
        assert expected_product_category == self.driver.title
