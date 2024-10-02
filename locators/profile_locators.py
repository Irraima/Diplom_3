from selenium.webdriver.common.by import By


class ProfileLocators:

    PROFILE_PAGE_BUTTON = By.XPATH, '//*[@href = "/account"]'
    PROFILE_BUTTON = By.XPATH, '//*[@href="/account/profile"]'
    HISTORY_BUTTON = By.XPATH, '//*[@href="/account/order-history"]'
    EXIT_BUTTON = By.XPATH, '//*[@href="/account/order-history"]/following::*[@type="button"][1]'
    ORDERS_AT_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, "
                                   "'text_type_digits-default')]")
