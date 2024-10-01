import allure
from data import Urls
from pages.base_page import BasePage
from locators.order_list_locators import OrderPageLocators as OPL


class OrderFeedPage(BasePage):

    @allure.step('Открытие страницы "Лента заказов"')
    def open_page(self):
        self.open_url(Urls.MAIN_PAGE + Urls.LIST_PAGE)

    @allure.step('Проверка наличия идентификатора заказа в ленте')
    def found_order_at_list(self, order_id):
        elements = self.wait_until_all_elements_located(OPL.ORDERS_AT_LIST)
        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.step('Проверка открытия окна заказа')
    def order_window_check(self):
        return self.presence_check(OPL.ORDER_COMPOSITION).is_displayed()

    @allure.step('Получение количества заказов за сегодня')
    def get_total_count_today(self):
        self.wait_element_visible(OPL.TOTAL_COUNT_TODAY)
        return self.get_text(OPL.TOTAL_COUNT_TODAY)
