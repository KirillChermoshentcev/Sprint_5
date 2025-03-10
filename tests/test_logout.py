from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators
from conftest import driver


class TestStellarBurgers:

    def test_logout(self, driver, timeout=10):
        email = Constants.EMAIL
        password = Constants.PASSWORD

        auth_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.AUTH_BUTTON_ACC))
        auth_button.click()

        email_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.EMAIL_FIELD))
        email_field.click()
        email_field.send_keys(email)

        password_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.PASSWORD_FIELD))
        password_field.click()
        password_field.send_keys(password)

        auth_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.AUTH_BUTTON_ENTER))
        auth_button.click()

        personal_account_btn = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC_BUTTON))
        personal_account_btn.click()

        logout_btn = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))
        logout_btn.click()

        enter = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(Locators.ENTER_TEXT)).text

        assert enter == Constants.ENTER


