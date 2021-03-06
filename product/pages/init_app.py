from product.pages.us.wildberries.ru.catalog_page import CatalogPage
from product.pages.us.wildberries.ru.components.navigate_bar import NavigateBar
from product.pages.us.wildberries.ru.home_page import HomePage
from product.pages.us.wildberries.ru.product_page import ProductPage

"""
This class initializes all pages of the application 
and allows us to use one object in tests to access all pages.
"""


class InitAppPages:
    def __init__(self, driver):
        self.home_page = HomePage(driver)
        self.catalog_page = CatalogPage(driver)
        self.product_page = ProductPage(driver)
        self.navigate_bar = NavigateBar(driver)
