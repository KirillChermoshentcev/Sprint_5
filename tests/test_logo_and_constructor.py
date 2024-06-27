from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators
from conftest import driver


class TestStellarBurgers:

    def test_click_on_constructor(self,driver):
        email = Constants.EMAIL
        password = Constants.PASSWORD

        auth_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.AUTH_BUTTON_ACC))
        auth_button.click()

        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.EMAIL))
        email_field.click()
        email_field.send_keys(email)

        password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PASSWORD))
        password_field.click()
        password_field.send_keys(password)

        auth_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.AUTH_BUTTON_ENTER))
        auth_button.click()

        personal_account_btn = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC_BUTTON))
        personal_account_btn.click()

        constructor_btn = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON))
        constructor_btn.click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_click_on_logo(self,driver):
        email = Constants.EMAIL
        password = Constants.PASSWORD

        auth_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.AUTH_BUTTON_ACC))
        auth_button.click()

        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.EMAIL))
        email_field.click()
        email_field.send_keys(email)

        password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PASSWORD))
        password_field.click()
        password_field.send_keys(password)

        auth_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.AUTH_BUTTON_ENTER))
        auth_button.click()

        personal_account_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC_BUTTON))
        personal_account_btn.click()

        logo_btn = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable(Locators.LOGO_BUTTON))
        logo_btn.click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

