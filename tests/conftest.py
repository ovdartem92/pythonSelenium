import json
import os
import sys
import allure
import pytest
from allure_commons.types import AttachmentType

from framework.browser.driver_factory import DriverFactory

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = ROOT_DIR + "\\config.json"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]


@pytest.fixture(scope='session')
def config():
    config_file = open(CONFIG_PATH)
    return json.load(config_file)


@pytest.fixture(scope="session")
def browser_setup(config):
    if "browser" not in config:
        raise Exception('The config file does not contain "browser"')
    elif config["browser"] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config["browser"]


@pytest.fixture(scope='session')
def wait_time_setup(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def website_setup(config):
    return config['tested_page'] if 'tested_page' in config else RuntimeError


@pytest.fixture()
def setup(request, config):
    driver = DriverFactory.get_driver(config["browser"], config["headless_mode"])
    driver.implicitly_wait(config["timeout"])
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    if config["browser"] == "firefox":
        driver.maximize_window()
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()
