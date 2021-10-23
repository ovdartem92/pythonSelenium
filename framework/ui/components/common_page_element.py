from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class CommonPageElement:
    def __init__(self, driver, locator_type, locator):
        if driver is None:
            driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver
        self.locator_type = locator_type
        self.locator = locator
