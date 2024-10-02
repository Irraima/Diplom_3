import allure
from pages.base_page import BasePage
from data import Urls
from locators.main_page_locators import MainPageLocators as MPL
from locators.order_list_locators import OrderPageLocators as OPL


class MainPage(BasePage):

    @allure.step('Открытие страницы регистрации')
    def open_reg_page(self):
        self.open_url(Urls.MAIN_PAGE + Urls.REGISTER)

    @allure.step('Открытие главной страницы')
    def open_main_page(self):
        self.open_url(Urls.MAIN_PAGE)

    @allure.step('Проверка открытия страницы после нажатия на кнопку "Лента Заказов"')
    def order_list_title_check(self):
        return self.exist_element_check(OPL.ORDER_PAGE_TITLE)

    @allure.step('Проверка открытия страницы после нажатия на кнопку "Конструктор"')
    def title_constructor_check(self):
        return self.exist_element_check(MPL.CONSTRUCTOR_TITLE)

    @allure.step('Проверка открытия окна ингредиента')
    def clickable_order_button_check(self):
        if self.wait_element_clickable(MPL.ORDER_LIST_BUTTON):
            return True
        else:
            return False

    @allure.step('Предусловие: открытие главной страницы, открытие окна ингредиента')
    def precondition_for_closing_window(self):
        self.open_main_page()
        self.click_element_if_clickable(MPL.R2_D3_BUN_BUTTON)

    @allure.step('Получение значения счетчика ингредиента')
    def get_count_value(self):
        return self.get_text(MPL.INGREDIENT_COUNTER)

    @allure.step('Перетаскивание ингредиента')
    def add_ingredient_to_order(self):
        self.wait_element_clickable(MPL.R2_D3_BUN_BUTTON)
        self.drag_and_drop_element(MPL.R2_D3_BUN_BUTTON, MPL.ORDERS_BASKET)

    @allure.step('Получение текста из окна с информацией об оформленном заказе')
    def placing_order_text_check(self):
        self.wait_element_visible(MPL.ORDER_ID_TEXT)
        return self.get_text(MPL.ORDER_ID_TEXT)

    @allure.step('Получение id заказа')
    def get_order_id(self):
        self.wait_element_visible(MPL.ORDER_ID_TEXT)
        order_id = self.get_text(MPL.ORDER_ID)
        while order_id == '9999':
            order_id = self.get_text(MPL.ORDER_ID)
        return f"{order_id}"
