import allure
from selenium.webdriver.common.by import By

from framework.ui.components.wrappers.button import Button
from product.pages.base_page import BasePage

"""
This is an example of the implementation of the page object pattern.
This class is the heir of base page
"""


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("[Wildberries Product Page] Open catalog page")
    def open_page(self):
        raise Exception("User should not open this page. User should choose a product")

    @allure.step("[Wildberries Product Page] Get product brand")
    def get_product_brand(self):
        locator = "//h1/span[@data-text='brand']"
        product_brand_field = self.driver.find_element(By.XPATH, locator)
        return product_brand_field.text

    @allure.step("[Wildberries Product Page] Click add to cart")
    def add_to_cart(self):
        locator = "//button[text()='Add to the cart']"
        button = Button(self.driver, By.XPATH, locator)
        button.click()

    @allure.step("[Wildberries Product Page] Select size")
    def select_size(self, size):
        locator = f"//ul[contains(@class,'size-list')]/li[text()='{size}']"
        button = Button(self.driver, By.XPATH, locator)
        button.click()

    @allure.step("[Wildberries Product Page] Check confirm message 'Product added to cart'")
    def check_confirm_message(self):
        locator = "//span[text()='Product added to cart']"
        element = self.driver.find_element(By.XPATH, locator)
        element.is_displayed()

    @allure.step("[Wildberries Product Page] Get basket items")
    def get_basket_items(self):
        locator = "//div[@class='basket-list']/div"
        elements = self.driver.find_elements(By.XPATH, locator)
        return elements
