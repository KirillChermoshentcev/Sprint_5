from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators
from conftest import driver


class TestStellarBurgers:

    def test_personal_account_click(self,driver):
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

        order_history_btn = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located(Locators.ORDER_HISTORY_BUTTON)).text
        assert order_history_btn == 'История заказов'



