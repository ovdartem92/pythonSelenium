import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

from product.pages.base_page import BasePage


class CatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("[Wildberries Home Page] Open home page")
    def open_page(self, config):
        self.driver.get(config["tested_page"])

    @allure.step("[Wildberries Home Page] Check that home page opened")
    def get_search_results(self):
        search_results = self.driver.find_elements(By.XPATH, "//div[@class='card-grid']/div")
        return search_results
