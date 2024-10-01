import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from locators.main_page_locators import MainPageLocators as MPL
from conftest import test_data


class TestMainPage:

    @allure.title('Открытие страницы "Конструктор"')
    def test_open_constructor_page(self, driver):
        mp = MainPage(driver)
        mp.open_reg_page()
        mp.click_element_if_clickable(MPL.CONSTRUCTOR_BUTTON)
        assert mp.title_constructor_check() is True, 'Не удалось перейти на страницу "Конструктор"'

    @allure.title('Открытие страницы "Лента заказов"')
    def test_open_order_list_page(self, driver):
        mp = MainPage(driver)
        mp.open_reg_page()
        mp.click_element_if_clickable(MPL.ORDER_LIST_BUTTON)
        assert mp.order_list_title_check() is True, 'Страница "Лента заказов" не открыта'

    @allure.title('Открытие окна ингредиента')
    def test_open_ingredient_window(self, driver):
        mp = MainPage(driver)
        mp.open_main_page()
        mp.click_element_if_clickable(MPL.R2_D3_BUN_BUTTON)
        assert mp.clickable_order_button_check() is True, 'Окно игридиента не открыто'

    @allure.title('Закрытие окна ингредиента')
    def test_close_ingredient_window(self, driver):
        mp = MainPage(driver)
        mp.precondition_for_closing_window()
        mp.click_element_if_clickable(MPL.CLOSE_BUTTON)
        assert mp.clickable_order_button_check() is True, 'Окно игридиента не закрыто'

    @allure.title('Проверка изменения счетчика ингредиента')
    def test_counter_add_ingredient(self, driver):
        mp = MainPage(driver)
        mp.open_main_page()
        pre_result = mp.get_count_value()
        mp.add_ingredient_to_order()
        post_result = mp.get_count_value()
        assert pre_result != post_result, 'Счетчик не изменился'

    @allure.title('Проверка возможности оформить заказ авторизованным пользователем')
    def test_placing_order(self, driver, test_data):
        pl = ProfilePage(driver)
        mp = MainPage(driver)

        pl.authorization(test_data)
        mp.add_ingredient_to_order()
        mp.click_element_if_clickable(MPL.ORDER_BUTTON)
        assert mp.placing_order_text_check() == 'идентификатор заказа', 'Оформить заказ не удалось'
