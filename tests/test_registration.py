from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

from conftest import driver



faker = Faker()

class UserData:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class TestStellarBurgers:
    def test_registration(self, driver, timeout=10, password='123456'):
        user = UserData(faker.name, faker.email)
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_LINK).click()

        # Ввод имени
        name_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.NAME_FIELD))
        name_field.click()
        name_field.send_keys(faker.name())

        # Ввод email
        email_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.EMAIL_FIELD))
        email_field.click()
        email_field.send_keys(faker.email())

        # Ввод пароля
        password_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.PASSWORD_FIELD))
        password_field.click()
        password_field.send_keys(password)

        # Нажатие кнопки "Зарегистрироваться"
        register_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.REGISTRATION_BUTTON))
        register_button.click()

        # Ожидание кнопки "Войти" и проверка наличия текста
        enter_form = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(Locators.AUTH_BUTTON_ENTER))
        assert enter_form.text == 'Войти'

    def test_incorrect_password(self,driver, timeout=10, password='12345'):
        user = UserData(faker.name, faker.email)
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_LINK).click()

        name_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.NAME_FIELD))
        name_field.click()
        name_field.send_keys(faker.name())

        email_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.EMAIL_FIELD))
        email_field.click()
        email_field.send_keys(faker.email())

        password_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.PASSWORD_FIELD))
        password_field.click()
        password_field.send_keys(password)

        register_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.REGISTRATION_BUTTON))
        register_button.click()

        incorrect_password = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(Locators.INCORRECT_PASSWORD))
        assert incorrect_password.text == 'Некорректный пароль'

    def test_incorrect_email(self,driver, timeout=10, password='123456' ):
        user = UserData(faker.name,email= 'qwerty@qwert')
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_LINK).click()

        name_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.NAME_FIELD))
        name_field.click()
        name_field.send_keys(faker.name())

        email_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.EMAIL_FIELD))
        email_field.click()
        email_field.send_keys(user.email)

        password_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.PASSWORD_FIELD))
        password_field.click()
        password_field.send_keys(password)

        register_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.REGISTRATION_BUTTON))
        register_button.click()

        incorrect_email = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(Locators.INCORRECT_EMAIL))
        assert incorrect_email.text == 'Такой пользователь уже существует'

    def test_namefield_can_not_be_empty(self,driver, timeout=10,name='', password='123456'):
        user = UserData(name,faker.email)
        driver.find_element(*Locators.PERSONAL_ACC_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_LINK).click()

        name_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.NAME_FIELD))
        name_field.click()
        name_field.send_keys(user.name)

        email_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.EMAIL_FIELD))
        email_field.click()
        email_field.send_keys(faker.email())

        password_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.PASSWORD_FIELD))
        password_field.click()
        password_field.send_keys(password)

        register_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(Locators.REGISTRATION_BUTTON))
        register_button.click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'