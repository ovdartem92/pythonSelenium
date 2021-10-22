from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ..components.common_page_element import CommonPageElement


class Button(CommonPageElement):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)

    def click(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.locator)))
        try:
            self.driver.find_element_by_xpath(self.locator).click()
        except StaleElementReferenceException:
            NotImplemented

    def get_text(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.locator)))
        return self.driver.find_element_by_xpath(self.locator).text
