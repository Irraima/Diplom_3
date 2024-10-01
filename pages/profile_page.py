import allure
from data import Urls
from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators as PL
from locators.login_locators import LoginLocators as LL
from conftest import test_data


class ProfilePage(BasePage):

    @allure.step('Проверка наличия элементов на открытой странице')
    def open_page_check(self):
        self.wait_element_visible(PL.PROFILE_BUTTON)
        return self.exist_element_check(PL.PROFILE_BUTTON)

    @allure.step('Открытие страницы "История заказов"')
    def open_history_page(self):
        self.wait_element_visible(PL.HISTORY_BUTTON)
        history_button = self.wait_element_visible(PL.HISTORY_BUTTON)
        self.driver.execute_script('arguments[0].click();', history_button)
        if self.get_url() == Urls.MAIN_PAGE + Urls.HISTORY_PAGE:
            return True
        else:
            return False

    @allure.step("Проверка наличия идентификатора заказа в истории")
    def found_order_at_history(self, order_id):
        elements = self.wait_until_all_elements_located(PL.ORDERS_AT_HISTORY)
        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.step('Нажатие кнопки "Выход" с проверкой выхода')
    def exit(self):
        exit_button = self.wait_element_visible(PL.EXIT_BUTTON)
        self.driver.execute_script('arguments[0].click();', exit_button)
        self.wait_element_not_visible(PL.EXIT_BUTTON)
        if self.get_url() == Urls.MAIN_PAGE + Urls.LOGIN:
            return True
        else:
            return False

    @allure.step('Авторизация')
    def authorization(self, test_data):
        name = test_data['name']
        password = test_data['password']
        email = test_data['email']
        self.open_url(Urls.MAIN_PAGE + Urls.REGISTER)
        self.wait_element_visible(LL.NAME_FIELD_FOR_REG)
        self.set_text(LL.NAME_FIELD_FOR_REG, name)
        self.set_text(LL.EMAIL_FIELD_FOR_REG, email)
        self.set_text(LL.PASSWORD_FIELD_FOR_REG, password)
        self.click_element_if_clickable(LL.REG_BUTTON)
        self.wait_element_not_visible(LL.REG_BUTTON)
        self.wait_element_visible(LL.EMAIL_FIELD_FOR_LOGIN)
        self.set_text(LL.EMAIL_FIELD_FOR_LOGIN, email)
        self.set_text(LL.PASSWORD_FIELD_FOR_LOGIN, password)
        self.click_element_if_clickable(LL.LOGIN_BUTTON)
        self.wait_element_not_visible(LL.LOGIN_BUTTON)

    def precondition_for_tests(self, test_data):
        self.authorization(test_data)
        self.click_element_if_clickable(PL.PROFILE_PAGE_BUTTON)
