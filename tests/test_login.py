from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators
from conftest import driver


class TestStellarBurgers:

    def test_login_from_main_page(self,driver, timeout=10):
        email = Constants.EMAIL
        password = Constants.PASSWORD

        auth_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.AUTH_BUTTON_ACC))
        auth_button.click()

        email_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.EMAIL))
        email_field.click()
        email_field.send_keys(email)

        password_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.PASSWORD))
        password_field.click()
        password_field.send_keys(password)

        auth_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.AUTH_BUTTON_ENTER))
        auth_button.click()

        make_order_btn = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(Locators.MAKE_ORDER_BUTTON)).text
        assert make_order_btn == 'Оформить заказ'

    def test_login_from_personal_account(self,driver, timeout=10):
        email = Constants.EMAIL
        password = Constants.PASSWORD

        personal_account_btn = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC_BUTTON))
        personal_account_btn.click()

        email_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.EMAIL))
        email_field.click()
        email_field.send_keys(email)

        password_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.PASSWORD))
        password_field.click()
        password_field.send_keys(password)

        auth_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.AUTH_BUTTON_ENTER))
        auth_button.click()

        make_order_btn = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(Locators.MAKE_ORDER_BUTTON)).text
        assert make_order_btn == 'Оформить заказ'

    def test_login_from_registration_page(self,driver,timeout=10):
        email = Constants.EMAIL
        password = Constants.PASSWORD

        personal_account_btn = WebDriverWait(driver,timeout).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC_BUTTON))
        personal_account_btn.click()

        register_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.REGISTRATION_LINK))
        register_button.click()

        enter = driver.find_element(*Locators.ENTER_LINK)
        driver.execute_script("arguments[0].scrollIntoView();", enter)
        enter.click()

        email_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.EMAIL))
        email_field.click()
        email_field.send_keys(email)

        password_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.PASSWORD))
        password_field.click()
        password_field.send_keys(password)

        auth_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.AUTH_BUTTON_ENTER))
        auth_button.click()

        make_order_btn = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(Locators.MAKE_ORDER_BUTTON)).text
        assert make_order_btn == 'Оформить заказ'

    def test_login_from_forgot_password_page(self,driver, timeout=10):
        email = Constants.EMAIL
        password = Constants.PASSWORD

        personal_account_btn = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACC_BUTTON))
        personal_account_btn.click()

        forgot_password = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.FORGOT_PASSWORD_LINK))
        driver.execute_script("arguments[0].scrollIntoView();", forgot_password)
        forgot_password.click()

        driver.find_element(*Locators.ENTER_LINK).click()

        email_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.EMAIL))
        email_field.click()
        email_field.send_keys(email)

        password_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.PASSWORD))
        password_field.click()
        password_field.send_keys(password)

        auth_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.AUTH_BUTTON_ENTER))
        auth_button.click()

        make_order_btn = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(Locators.MAKE_ORDER_BUTTON)).text
        assert make_order_btn == 'Оформить заказ'





