import datetime
import logging
import os
import shutil

from selenium.webdriver.support.events import AbstractEventListener

from framework.utils.utils import get_project_root

'''
This class monitors the actions of the web driver and logs it.
'''

LOG_NAME = datetime.datetime.now().strftime("%d-%m-%Y__%H-%M-%S")
REPORT_PATH = rf"{get_project_root()}\\report\\"
if os.path.exists(REPORT_PATH):
    shutil.rmtree(REPORT_PATH)
os.mkdir(REPORT_PATH)
logging.basicConfig(
    filename=f"{REPORT_PATH + LOG_NAME}.logs",
    format="%(asctime)s: %(levelname)s: %(message)s",
    level=logging.INFO
)


class WebDriverListener(AbstractEventListener):
    def __init__(self):
        self.logger = logging.getLogger("selenium")

    def before_navigate_to(self, url, driver):
        self.logger.info(f"Navigating to {url}")

    def after_navigate_to(self, url, driver):
        self.logger.info(f"Navigated to {url}")

    def before_find(self, by, value, driver):
        self.logger.info(f"Searching for element by {by} {value}")

    def after_find(self, by, value, driver):
        self.logger.info(f"Element by {by} {value} found")

    def before_click(self, element, driver):
        if element.get_attribute("text") is None:
            self.logger.info(f"Clicking on {element.get_attribute('class')}")
        else:
            self.logger.info(f"Clicking on {element.get_attribute('text')}")

    def after_click(self, element, driver):
        if element.get_attribute("text") is None:
            self.logger.info(f"{element.get_attribute('class')} clicked")
        else:
            self.logger.info(f"{element.get_attribute('text')} clicked")

    def before_change_value_of(self, element, driver):
        self.logger.info(f"{element.get_attribute('text')} value changed")

    def before_quit(self, driver):
        self.logger.info("Driver quitting")

    def after_quit(self, driver):
        self.logger.info("Driver quitted")

    def on_exception(self, exception, driver):
        self.logger.info(exception)
