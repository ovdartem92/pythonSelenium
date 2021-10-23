import allure
import pytest

from product.pages.us.wildberries.ru.home_page import HomePage


# @pytest.mark.skip()
@pytest.mark.usefixtures("setup")
class TestOne:
    @allure.epic("Training epic")
    @allure.title("Check that user can enter to Clothes product category")
    @allure.severity("High")
    @allure.testcase("https://goldcast.atlassian.net/browse/AM-468",
                     "Check Agenda, Sanity Agenda, AM-382, AM-379, Video QnA, AM-381, AM-346")
    @allure.description("Open home page, choose product category to For Women > Clothes, "
                        "check that the title on page is Clothes")
    def test_open_home_page(self, config):
        home_page = HomePage(self.driver)
        home_page.open_page(config)
        home_page.click_agree_button()
        home_page.check_home_page_opened(config)
        home_page.click_burger_menu()
        home_page.choose_product_category("For women")
        home_page.choose_product_category("Clothes")
        assert "Clothes" == self.driver.title
