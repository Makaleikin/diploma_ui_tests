import os

import allure
from selene.support.shared import browser
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attachments


@allure.step('Конфигурация теста')
@pytest.fixture(scope='function', autouse=True)
def test_browser_configuration():
    browser.config.base_url = os.getenv('selene.base_url', 'https://www.tesla.com')
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    yield
    attachments.add_html(browser)
    attachments.add_screenshot(browser)
    attachments.add_logs(browser)
    attachments.add_video(browser)
