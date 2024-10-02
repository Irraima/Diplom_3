from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR_TITLE = (By.XPATH, '//*[text() = "Соберите бургер"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//*[text() = "Конструктор"]')
    ORDER_LIST_BUTTON = (By.XPATH, '//p[contains(.,"Лента Заказов")]')
    R2_D3_BUN_BUTTON = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
    ORDER_BUTTON = (By.XPATH, '//*[text()="Оформить заказ"]')
    ORDER_ID_TEXT = (By.XPATH, '//p[text()="идентификатор заказа"]')
    ORDER_ID = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')
    CLOSE_BUTTON = (By.XPATH, '//button[contains(@class,"close")]')
    INGREDIENT_WINDOW_TITLE = (By.XPATH, '//*[text() = "Детали ингредиента"]')
    INGREDIENT_COUNTER = (By.XPATH, './/p[contains(@class, "counter_counter")]')
    ORDERS_BASKET = (By.XPATH, '//li[2][contains(@class, "BurgerConstructor_basket__listItem")]')
