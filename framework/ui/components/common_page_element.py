from abc import ABC as abstract_class

"""
This is an abstract class containing the common fields of a web element.
"""


class CommonPageElement(abstract_class):
    def __init__(self, driver, locator_type, locator):
        self.driver = driver
        self.locator_type = locator_type
        self.locator = locator
