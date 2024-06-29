from selenium.webdriver.common.by import By


class Locators:

    EMAIL = (By.XPATH, '//label[contains(text(),"Email")]/following-sibling::input')  #Поле для ввода Email
    PASSWORD = (By.XPATH, '//label[contains(text(),"Пароль")]/following-sibling::input')  #Поле для ввода пароля
    AUTH_BUTTON_ACC = (By.XPATH, '//button[contains(text(),"Войти в аккаунт")]')  #Кнопка Войти в аккаунт на главной странице при незалогине
    AUTH_BUTTON_ENTER = (By.XPATH, '//button[contains(text(),"Войти")]')  #Кнопка Войти под полями логина
    ENTER_LINK = (By.XPATH, '//p/a[@href="/login"]')  #Ссылка Войти под формой регистрации
    PERSONAL_ACC_BUTTON = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')  #Кнопка перехода в Личный кабинет
    FORGOT_PASSWORD_LINK = (By.XPATH, '//p/a[@href="/forgot-password"]')  #Ссылка на страницу восстановления пароля
    REGISTRATION_BUTTON = (By.XPATH, '//button[contains(text(),"Зарегистрироваться")]')  #Кнопка "Зарегистрироваться"
    REGISTRATION_LINK = (By.XPATH, '//p/a[@href="/register"]')  #Ссылка на страницу регистрации под формой залогина
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(text(),"Выход")]')  #Кнопка выхода в личном кабинете
    ENTER_TEXT = (By.XPATH, '//h2[contains(text(),"Вход")]') #Локатор текста "Вход" на странице залогина

    MAKE_ORDER_BUTTON = (By.XPATH, '//button[contains(text(),"Оформить заказ")]') #Кнопка "Оформить заказ"
    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[contains(text(),"История заказов")]')  #Кнопка "История заказов"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[contains(text(),"Конструктор")]') #Страница конструктора

    LOGO_BUTTON = (By.XPATH, '//div/a[@href= "/"]')  #Логотип Stellar Burgers

    SAUCE_TAB = (By.XPATH, '//span[contains(text(),"Соусы")]')  #Вкладка соусы в конструкторе
    FILLINGS_TAB = (By.XPATH, '//span[contains(text(),"Начинки")]')  #Вкладка начинки в конструкторе
    BUNS_TAB = (By.XPATH, '//span[contains(text(),"Булки")]')  #Вкладка булки в конструкторе

    ACTIVE_TAB = (By.XPATH,'//div[contains(@class, "tab_tab__") and contains(@class, "tab_tab_type_current__")]')  #Локатор активной вкладки в конструкторе
