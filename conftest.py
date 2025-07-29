import os
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from data.urls import BASE_URL

SELENIUM_URI = os.getenv("SELENIUM_URI", "http://selenium:4444/wd/hub")

@pytest.fixture()
def driver():
    options = ChromeOptions()
    options.add_argument("--window-size=2560,1440")
    options.set_capability("acceptInsecureCerts", True)

    driver = webdriver.Remote(
        command_executor=SELENIUM_URI,
        options=options
    )

    driver.get(BASE_URL)
    yield driver
    driver.quit()
