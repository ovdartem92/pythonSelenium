from abc import abstractmethod, ABC as abstract_class

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

"""
This is an abstract class Base Page
All Page object objects must inherit from this class
"""


class BasePage(abstract_class):
    def __init__(self, driver):
        if driver is None:
            driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver

    @abstractmethod
    def open_page(self, config):
        pass
