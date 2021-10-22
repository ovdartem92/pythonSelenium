import allure

from framework.ui.components.button import Button
from framework.ui.components.text_field import TextField
from product.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click to logo button")
    def click_to_logo(self):
        Button(self.driver, "//a[@id='ybar-logo']").click()

    @allure.step("Click to search button")
    def click_to_search_button(self):
        Button(self.driver, "//input[@id='ybar-search']").click()

    @allure.step("Type text to search input")
    def type_text_to_search_input(self, text):
        TextField(self.driver, "//input[@id='ybar-sbq']").type(text)

    def click_to_mail_tab(self):
        Button(self.driver, "//div[@id='ybar-navigation']//a[normalize-space()='Mail']").click()