import allure
from selenium.webdriver.common.by import By

from framework.ui.components.wrappers.button import Button
from product.pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("[Wildberries Product Page] Open catalog page")
    def open_page(self):
        raise Exception("User should choose a product")

    @allure.step("[Wildberries Product Page] Get product brand")
    def get_product_brand(self):
        product_brand_field = self.driver.find_element(By.XPATH, "//h1/span[@data-text='brand']")
        return product_brand_field.text

    @allure.step("[Wildberries Product Page] Click add to cart")
    def click_add_to_cart(self):
        button = Button(self.driver, By.XPATH, "//button[text()='Add to the cart']")
        button.click()
