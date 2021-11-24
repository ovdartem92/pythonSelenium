import json

import allure
import pytest
from allure_commons.types import AttachmentType

from framework.browser.driver_factory import DriverFactory
from framework.utils.utils import get_project_root

"""
This is the main class for running tests. 
It contains the fixtures. We use fixtures each times when run our tests.
"""

CONFIG_PATH = f"{get_project_root()}\\config.json"
DEFAULT_WAIT_TIME = 5
SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]


@pytest.fixture(scope='session')
def config():
    config_file = open(CONFIG_PATH)
    return json.load(config_file)


@pytest.fixture(scope='session')
def wait_time_setup(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture()
def setup(request, config):
    driver = DriverFactory.get_driver(config["browser"], config["headless_mode"])
    driver.implicitly_wait(config["timeout"])
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    if config["browser"] is not None:
        driver.maximize_window()
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()


@pytest.fixture()
def api(request, config):
    base_uri = config["base_URI"]
    request.cls.base_uri = base_uri
