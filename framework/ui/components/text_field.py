from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ..components.common_page_element import CommonPageElement


class TextField(CommonPageElement):
    def __init__(self, driver, locator_type, locator):
        super().__init__(driver, locator_type, locator)

    def type(self, text):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.locator_type, self.locator)))
        self.driver.find_element(self.locator_type, self.locator).send_keys(text)

    def clear(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((self.locator_type, self.locator)))
        self.driver.find_element(self.locator_type, self.locator).clear()
