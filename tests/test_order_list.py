import allure
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from pages.profile_page import ProfilePage
from locators.main_page_locators import MainPageLocators as MPL
from locators.profile_locators import ProfileLocators as PL
from locators.order_list_locators import OrderPageLocators as OPL


class TestOrderList:

    @allure.title('Проверка открытия окна с информацией о заказе')
    def test_open_order_window(self, driver):
        olp = OrderListPage(driver)
        olp.open_page()
        olp.click_element_if_clickable(OPL.ORDER_OBJECT)
        return olp.order_window_check() is True, 'Окно не открыто'

    @allure.title('Проверка совпадения id в ленте заказов и в истории заказов')
    def test_find_order_id_in_list(self, driver, test_data):
        pp = ProfilePage(driver)
        olp = OrderListPage(driver)
        mp = MainPage(driver)

        pp.authorization(test_data)
        mp.add_ingredient_to_order()
        mp.click_element_if_clickable(MPL.ORDER_BUTTON)
        order_id = mp.get_order_id()
        mp.click_element_if_clickable(MPL.CLOSE_BUTTON)
        pp.click_element_if_clickable(PL.PROFILE_PAGE_BUTTON)
        pp.open_history_page()
        order_id_in_history = pp.found_order_at_history(order_id)
        mp.click_element_if_clickable(MPL.ORDER_LIST_BUTTON)
        order_id_in_order_list = olp.found_order_at_list(order_id)
        assert order_id_in_order_list and order_id_in_history is True, 'Id не совпадают'

    @allure.title('Проверка изменения счетчика заказов за сегодня')
    def test_today_orders_counter(self, driver, test_data):
        pp = ProfilePage(driver)
        olp = OrderListPage(driver)
        mp = MainPage(driver)

        pp.authorization(test_data)
        mp.click_element_if_clickable(MPL.ORDER_LIST_BUTTON)
        pre_count = olp.get_total_count_today()
        mp.click_element_if_clickable(MPL.CONSTRUCTOR_BUTTON)
        mp.add_ingredient_to_order()
        mp.click_element_if_clickable(MPL.ORDER_BUTTON)
        mp.click_element_if_clickable(MPL.CLOSE_BUTTON)
        mp.click_element_if_clickable(MPL.ORDER_LIST_BUTTON)
        post_count = olp.get_total_count_today()
        assert post_count > pre_count, 'Счетчик не изменился'

    @allure.title('Проверка появления созданного заказа в ленте заказов')
    def test_new_order_at_order_list(self, driver, test_data):
        pp = ProfilePage(driver)
        olp = OrderListPage(driver)
        mp = MainPage(driver)

        pp.authorization(test_data)
        mp.add_ingredient_to_order()
        mp.click_element_if_clickable(MPL.ORDER_BUTTON)
        order_id = mp.get_order_id()
        mp.click_element_if_clickable(MPL.CLOSE_BUTTON)
        mp.click_element_if_clickable(MPL.ORDER_LIST_BUTTON)
        assert olp.found_order_at_list(order_id) is True
