from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR_TITLE = (By.XPATH, '//*[text() = "Соберите бургер"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//*[text() = "Конструктор"]')
    ORDER_LIST_BUTTON = (By.XPATH, '//p[contains(.,"Лента Заказов")]')
    R2_D3_BUN_BUTTON = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
    ORDER_BUTTON = (By.XPATH, '//*[text()="Оформить заказ"]')
    ORDER_ID_TEXT = (By.XPATH, '//p[text()="идентификатор заказа"]')
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    CLOSE_BUTTON = (By.XPATH, '//button[contains(@class,"close")]')
    INGREDIENT_WINDOW_TITLE = (By.XPATH, '//*[text() = "Детали ингредиента"]')
    INGREDIENT_COUNTER = (By.XPATH, './/p[contains(@class, "counter_counter")]')
    ORDERS_BASKET = (By.XPATH, '/html/body/div/div/main/section[2]/ul/li[2]')
