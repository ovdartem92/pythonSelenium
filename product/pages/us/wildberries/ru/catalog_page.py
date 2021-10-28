import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

from product.pages.base_page import BasePage


class CatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("[Wildberries Catalog Page] Open catalog page")
    def open_page(self):
        raise Exception("User should choose a product")

    @allure.step("[Wildberries Catalog Page] Get array with search result")
    def get_search_results(self):
        search_results = self.driver.find_elements(By.XPATH, "//div[@class='card-grid']/div")
        return search_results

    @allure.step("[Wildberries Catalog Page] Get array with search result")
    def click_to_search_result_by_number_of_search(self, search_result_array, number):
        try:
            search_result_array[number].click()
        except StaleElementReferenceException:
            pass
