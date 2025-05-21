# drivers/driver_factory.py
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_remote_driver():
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['enableVNC'] = True
    capabilities['enableVideo'] = False

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=capabilities
    )
    driver.maximize_window()
    return driver
