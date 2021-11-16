from abc import abstractmethod


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def open_page(self, config):
        pass
