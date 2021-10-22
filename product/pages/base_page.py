import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    def __init__(self, driver):
        if driver is None:
            driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver

    @allure.step("[BASE PAGE] Open Home Page")
    def open_home_page(self, config):
        self.driver.get(config["tested_page"])

    @allure.step("[BASE PAGE] Check that Home Page opened")
    def check_home_page_opened(self, config):
        actual_url = self.driver.current_url
        expected_url = config["tested_page"]
        assert actual_url == expected_url
