from selenium.webdriver.common.by import By


class LoginLocators:

    RESTORE_PASSWORD_BUTTON = (By.XPATH, '//*[text() = "Восстановить пароль"]')
    LOGIN_BUTTON = By.XPATH, '//button[text() = "Войти"]'
    REG_BUTTON = By.XPATH, '//button[text() = "Зарегистрироваться"]'
    EMAIL_FIELD_FOR_LOGIN = By.XPATH, '//*[@name = "name"]'
    PASSWORD_FIELD_FOR_LOGIN = By.XPATH, '//*[@name = "Пароль"]'
    NAME_FIELD_FOR_REG = By.XPATH, '//*[text()="Регистрация"]/following::*[@name = "name"][1]'
    EMAIL_FIELD_FOR_REG = (By.XPATH, '//*[text()="Регистрация"]/following::*[@name = "name"][2]')
    PASSWORD_FIELD_FOR_REG = (By.XPATH, "//*[@name  = \"Пароль\"]")
