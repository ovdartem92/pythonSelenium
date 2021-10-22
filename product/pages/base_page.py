import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from abc import abstractmethod


class BasePage:
    def __init__(self, driver):
        if driver is None:
            driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver

    @abstractmethod
    def open_page(self, config):
        pass

    @allure.step("[Navigation Panel] Click burger menu")
    def click_burger_menu(self):
        button = self.driver.find_element(By.XPATH, "//button[@aria-label='Main menu']")
        button.click()

    @allure.step("[Navigation Panel] Click user menu")
    def click_user_menu(self):
        button = self.driver.find_element(By.XPATH, "//button[@class='user-menu__btn']")
        button.click()    \

    @allure.step("[Navigation Panel] Click logo")
    def click_user_menu(self):
        button = self.driver.find_element(By.XPATH, "//a[@class='header__logo']")

        button.click()

    @allure.step("[Navigation Panel] Click cart")
    def click_cart(self):
        button = self.driver.find_element(By.XPATH, "//a[@class='basketLink']")
        button.click()

    @allure.step("[Navigation Panel] Type text to search input")
    def type_text_to_search(self, text):
        search_input = self.driver.find_element(By.ID, "search-input")
        search_input.send_keys(text)
