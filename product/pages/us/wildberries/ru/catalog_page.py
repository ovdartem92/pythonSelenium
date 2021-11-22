import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

from product.pages.base_page import BasePage

"""
This is an example of the implementation of the page object pattern.
This class is the heir of base page
"""


class CatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("[Wildberries Catalog Page] Open catalog page")
    def open_page(self):
        raise Exception("User should not open this page.")

    @allure.step("[Wildberries Catalog Page] Get array with search result")
    def get_search_results(self):
        locator = "//div[@class='card-grid']/div"
        search_results = self.driver.find_elements(By.XPATH, locator)
        return search_results

    @allure.step("[Wildberries Catalog Page] Get array with search result")
    def click_to_search_result_by_number_of_search(self, search_result_array, number):
        try:
            search_result_array[number].click()
        except StaleElementReferenceException:
            pass
