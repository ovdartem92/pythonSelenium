from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from framework.ui.components.common_page_element import BaseWebElement

"""
This is a wrapper class that wraps methods that can be used when working with a text field.
"""


class TextField(BaseWebElement):
    def __init__(self, driver, locator_type, locator):
        super().__init__(driver, locator_type, locator)

    def type(self, text):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.locator_type, self.locator)))
        self.driver.find_element(self.locator_type, self.locator).send_keys(text)

    def clear(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.locator_type, self.locator)))
        self.driver.find_element(self.locator_type, self.locator).clear()
