from abc import abstractmethod

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    def __init__(self, driver):
        if driver is None:
            driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver

    @abstractmethod
    def open_page(self, config):
        pass
