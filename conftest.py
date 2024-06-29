import pytest
from selenium import webdriver
import faker

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
    driver.find_element(*Locators.AUTH_BUTTON_ENTER).click()
    return driver

@pytest.fixture
def user_data():
    return UserData(name= faker.name(), email= faker.email(), password='123456')

