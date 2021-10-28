from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from product.pages.us.wildberries.ru.catalog_page import CatalogPage
from product.pages.us.wildberries.ru.home_page import HomePage
from product.pages.us.wildberries.ru.product_page import ProductPage
from product.pages.us.wildberries.ru.components.navigate_bar import NavigateBar


class InitPage:
    def __init__(self, driver):
        if driver is None:
            driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver
        self.home_page = HomePage(self.driver)
        self.catalog_page = CatalogPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.navigate_bar = NavigateBar(self.driver)
