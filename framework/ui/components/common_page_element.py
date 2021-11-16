class CommonPageElement:
    def __init__(self, driver, locator_type, locator):
        self.driver = driver
        self.locator_type = locator_type
        self.locator = locator
