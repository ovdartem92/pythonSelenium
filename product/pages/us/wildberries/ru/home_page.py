import allure
from selenium.webdriver.common.by import By

from framework.ui.components.button import Button
from product.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("[Wildberries Home Page] Open home page")
    def open_page(self, config):
        self.driver.get(config["tested_page"])

    @allure.step("[Wildberries Home Page] Check that home page opened")
    def check_home_page_opened(self, config):
        actual_url = self.driver.current_url
        expected_url = config["tested_page"]
        assert actual_url == expected_url

    @allure.step("[Wildberries Home Page] Click I agree button")
    def click_agree_button(self):
        button = Button(self.driver, By.XPATH, "//button[text()='I agree']")
        button.click()

    @allure.step("[Wildberries Home Page] Choose product category by name")
    def choose_product_category(self, product_category):
        button_with_product_name = Button(self.driver, By.XPATH, f"//li/span[text()='{product_category}']")
        button_with_product_name.click()
