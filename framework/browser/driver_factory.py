from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.edge.service import Service as ServiceEdge
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from framework.listener.web_driver_listener import WebDriverListener
from framework.utils.utils import get_project_root

"""
This class is required to create and get a driver object.
The driver object helps us work with the browser.
This class has only one static method.
"""


class DriverFactory:
    """
    This method helps us to get instance of browser.
    You should pass two parameters:
    the first - the browser type: in string format,
    the second - the headless mode: in boolean format
    """

    @staticmethod
    def get_driver(browser, headless_mode=False) -> EventFiringWebDriver:
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            service = ServiceChrome(executable_path=ChromeDriverManager().install())
            if headless_mode is True:
                options.add_argument("--headless")
            driver = EventFiringWebDriver(webdriver.Chrome(service=service, options=options), WebDriverListener())
            return driver

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            service = ServiceFirefox(executable_path=GeckoDriverManager().install(),
                                     log_path=f"{get_project_root()}\\report\\geckodriver.log")
            if headless_mode is True:
                options.headless = True
            driver = EventFiringWebDriver(
                webdriver.Firefox(service=service, options=options),
                WebDriverListener())
            return driver

        elif browser == "edge":
            options = webdriver.EdgeOptions()
            options.use_chromium = True
            service = ServiceEdge(executable_path=EdgeChromiumDriverManager().install())
            if headless_mode is True:
                options.headless = True
            driver = EventFiringWebDriver(
                webdriver.Edge(service=service, options=options),
                WebDriverListener()
            )
            return driver

        raise Exception("Provide valid driver name")
