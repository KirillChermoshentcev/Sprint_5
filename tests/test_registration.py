from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


faker = Faker()


class TestStellarBurgers:
    def test_registration(self, driver):
        name = faker.name()
        email = faker.email()
        password = '123456'
        print(email)
        driver.find_element(By.XPATH, '//p[contains(text(),"Личный Кабинет")]').click()
        driver.find_element(By.XPATH, '//a[contains(text(),"Зарегистрироваться")]').click()

        # Ввод имени
        name_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"Имя")]/following-sibling::input')))
        name_field.click()
        name_field.send_keys(name)

        # Ввод email
        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"Email")]/following-sibling::input')))
        email_field.click()
        email_field.send_keys(email)

        # Ввод пароля
        password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"Пароль")]/following-sibling::input')))
        password_field.click()
        password_field.send_keys(password)

        # Нажатие кнопки "Зарегистрироваться"
        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Зарегистрироваться")]')))
        register_button.click()

        # Ожидание кнопки "Войти" и проверка наличия текста
        enter_form = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//button[contains(text(),"Войти")]')))
        assert enter_form.text == 'Войти'

    def test_incorrect_password(self,driver):
        name = faker.name()
        email = faker.email()
        password = '12345'
        driver.find_element(By.XPATH, '//p[contains(text(),"Личный Кабинет")]').click()
        driver.find_element(By.XPATH, '//a[contains(text(),"Зарегистрироваться")]').click()

        name_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"Имя")]/following-sibling::input')))
        name_field.click()
        name_field.send_keys(name)

        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"Email")]/following-sibling::input')))
        email_field.click()
        email_field.send_keys(email)

        password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"Пароль")]/following-sibling::input')))
        password_field.click()
        password_field.send_keys(password)

        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Зарегистрироваться")]')))
        register_button.click()

        incorrect_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//p[contains(text(),"Некорректный пароль")]')))
        assert incorrect_password.text == 'Некорректный пароль'

    def test_incorrect_email(self,driver):
        name = faker.name()
        email = 'qwerty@qwert'
        password = '123456'
        driver.find_element(By.XPATH, '//p[contains(text(),"Личный Кабинет")]').click()
        driver.find_element(By.XPATH, '//a[contains(text(),"Зарегистрироваться")]').click()

        name_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"Имя")]/following-sibling::input')))
        name_field.click()
        name_field.send_keys(name)

        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"Email")]/following-sibling::input')))
        email_field.click()
        email_field.send_keys(email)

        password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"Пароль")]/following-sibling::input')))
        password_field.click()
        password_field.send_keys(password)

        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Зарегистрироваться")]')))
        register_button.click()

        incorrect_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//p[contains(text(),"Такой пользователь уже существует")]')))
        assert incorrect_email.text == 'Такой пользователь уже существует'

    def test_namefield_can_not_be_empty(self,driver):
        name = ''
        email = faker.email()
        password = '123456'
        driver.find_element(By.XPATH, '//p[contains(text(),"Личный Кабинет")]').click()
        driver.find_element(By.XPATH, '//a[contains(text(),"Зарегистрироваться")]').click()

        name_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"Имя")]/following-sibling::input')))
        name_field.click()
        name_field.send_keys(name)

        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"Email")]/following-sibling::input')))
        email_field.click()
        email_field.send_keys(email)

        password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"Пароль")]/following-sibling::input')))
        password_field.click()
        password_field.send_keys(password)

        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Зарегистрироваться")]')))
        register_button.click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'