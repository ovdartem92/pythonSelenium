import allure

from framework.ui.components.button import Button
from product.pages.base_page import BasePage


class MailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click to logo button")
    def click_to_logo(self):
        Button(self.driver, "//span[@class='column']/a").click()

    @allure.step("Click to next button")
    def click_to_next(self):
        self.driver.find_element_by_id('login-signin').click()

    @allure.step("Click to let's go button")
    def click_to_lets_go(self):
        self.driver.find_element_by_xpath("//div[@class='section']/a").click()

    @allure.step("Type text to email input")
    def type_to_login_input(self, text):
        self.driver.find_element_by_css_selector('.input-group input').send_keys(text)

    @allure.step("Check that logo is visible")
    def check_mail_logo_is_displayed(self):
        self.driver.find_element_by_id('ybar-logo').is_displayed()
