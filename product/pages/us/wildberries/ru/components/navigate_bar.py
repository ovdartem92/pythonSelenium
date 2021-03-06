import allure
from selenium.webdriver.common.by import By

from framework.ui.components.wrappers.button import Button
from framework.ui.components.wrappers.text_field import TextField

"""
This is a class-navigated bar. It is displayed on every page
"""


class NavigateBar:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("[Navigation Panel] Click burger menu")
    def click_burger_menu(self):
        button = Button(self.driver, By.XPATH, "//button[@aria-label='Main menu']")
        button.click()

    @allure.step("[Navigation Panel] Click user menu")
    def click_user_menu(self):
        button = Button(self.driver, By.XPATH, "//button[@class='user-menu__btn']")
        button.click()

    @allure.step("[Navigation Panel] Click logo")
    def click_logo(self):
        button = Button(self.driver, By.XPATH, "//a[@class='header__logo']")
        button.click()

    @allure.step("[Navigation Panel] Click cart")
    def click_cart(self):
        button = Button(self.driver, By.XPATH, "//a[@class='basketLink']")
        button.click()

    @allure.step("[Navigation Panel] Type text to search input")
    def type_text_to_search(self, text):
        search_input = TextField(self.driver, By.ID, "search-input")
        search_input.type(text)
