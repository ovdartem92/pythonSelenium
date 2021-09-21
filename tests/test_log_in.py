import pytest
import allure
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup", "website_setup")
class TestLogIn:

    @allure.title("Login with valid data test")
    @allure.description("This is test of login with valid data")
    def test_login_passed(self, config):
        homePage = HomePage(self.driver)
        homePage.open_home_page(config)

    # @allure.title("Login with invalid email test")
    # @allure.description("This is test of login with invalid email")
    # def test_login_failed(self, config):
    #     log_in_page = LogInPage(self.driver)
    #     log_in_page.open_home_page(config)
    #     log_in_page.expand_account_menu()
    #     log_in_page.open_login_page()
    #     log_in_page.set_user_inputs("admin@phptravels.com", "demouser")
    #     error_msg = "Invalid Email or Password"
    #     assert error_msg in self.driver.find_element(*LogInLocators.invalid_data_msg).text


