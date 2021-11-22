from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from framework.ui.components.common_page_element import CommonPageElement

"""
This is a wrapper class that wraps methods that can be used when working with a button.
"""


class Button(CommonPageElement):
    def __init__(self, driver, locator_type, locator):
        super().__init__(driver, locator_type, locator)

    def click(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((self.locator_type, self.locator)))
        try:
            self.driver.find_element(self.locator_type, self.locator).click()
        except StaleElementReferenceException:
            pass

    def get_text(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.locator_type, self.locator)))
        return self.driver.find_element_by_xpath(self.locator).text()
