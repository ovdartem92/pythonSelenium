import allure
import pytest

from product.pages.com.yahoo.home_page import HomePage
from product.pages.com.yahoo.mail_page import MailPage


@pytest.mark.usefixtures("setup", "website_setup")
class Test:

    @allure.title("Open home page, click mail tab, click logo button")
    @allure.description("Open home page and check that url as in config file")
    def test_second(self, config):
        home_page = HomePage(self.driver)
        mail_page = MailPage(self.driver)
        home_page.open_home_page(config)
        home_page.click_to_mail_tab()

        mail_page.click_to_lets_go()
        mail_page.type_to_login_input("ovd.artem")
        mail_page.click_to_next()
        mail_page.type_to_login_input("Brilliance123")
        mail_page.click_to_next()
        mail_page.check_mail_logo_is_displayed()
