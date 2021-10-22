from ..components.common_page_element import CommonPageElement


class TextField(CommonPageElement):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)

    def type(self, text):
        self.driver.find_element_by_xpath(self.locator).send_keys(text)

    def clear(self):
        self.driver.find_element_by_xpath(self.locator).clear()
