from selenium.webdriver.common.by import By


class RestoreLocators:

    RESTORE_PASSWORD_TITLE = (By.XPATH, '//*[text() = "Восстановление пароля"]')
    EMAIL_FILED = (By.XPATH, '//*[@name = "name"]')
    PASSWORD_FILED = (By.XPATH, '//*[@name="Введите новый пароль"]')
    STROKE_ACTIVE_PASSWORD_FILED = (By.XPATH, ".//div[contains(@class,'input_status_active')]")
    ACTIVE_PASSWORD_FILED = (By.XPATH, ".//label[contains(@class,'input__placeholder-focused')]")
    RESTORE_BUTTON = (By.XPATH, '//*[text() = "Восстановить"]')
    SHOW_HIDE_BUTTON = (By.XPATH, ".//div[contains(@class, 'input__icon')]/*[name()='svg']")
