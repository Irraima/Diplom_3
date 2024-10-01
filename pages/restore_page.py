import allure
from pages.base_page import BasePage
from locators.restore_locators import RestoreLocators as RL
from conftest import test_data
from data import Urls


class RestorePasswordPage(BasePage):

    @allure.step('Открытие страницы "Восстановление пароля"')
    def open_forgot_password_page(self):
        self.open_url(f'{Urls.MAIN_PAGE}{Urls.FORGOT_PASSWORD}')

    @allure.step('Получение заголовка')
    def title_check(self):
        return self.exist_element_check(RL.RESTORE_PASSWORD_TITLE)

    @allure.step('Ввод данных в поле ввода "Email"')
    def input_email(self, test_data):
        self.set_text(RL.EMAIL_FILED, test_data['email'])

    @allure.step('Проверка наличия поля ввода "Пароль"')
    def exist_password_field_check(self):
        return self.exist_element_check(RL.PASSWORD_FILED)

    @allure.step('Ввод данных в поле "Пароль"')
    def input_password(self, test_data):
        self.set_text(RL.PASSWORD_FILED, test_data['password'])

    @allure.step('Получение статуса обводки поля ввода "Пароль"')
    def stroke_password_field_check(self):
        if self.wait_element_visible(RL.ACTIVE_PASSWORD_FILED):
            return True

    @allure.step('Получение статуса поля ввода "Пароль"')
    def active_password_field_check(self):
        if self.wait_element_visible(RL.ACTIVE_PASSWORD_FILED):
            return True

    @allure.step('Предусловие для кнопки "Показать/скрыть"')
    def precondition_for_show_hide_button(self, test_data):
        self.open_forgot_password_page()
        self.input_email(test_data)
        self.click_element_if_clickable(RL.RESTORE_BUTTON)
