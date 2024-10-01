from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_PAGE_TITLE = (By.XPATH, '//*[text() = "Лента заказов"]')
    ORDER_OBJECT = (By.XPATH, '//*[contains(@class, "OrderHistory_link")]')
    ORDER_COMPOSITION = By.XPATH, '//*[text()="Cостав"]'
    ORDERS_AT_LIST = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                                "text_type_digits-default']")
    TOTAL_COUNT_TODAY = (By.XPATH, '//*[text() = "Выполнено за сегодня:"]/following::*[@class][1]')
