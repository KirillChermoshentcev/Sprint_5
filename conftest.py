import pytest
from selenium import webdriver

from constants import Constants
from locators import Locators


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Constants.URL)
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)

    return driver
