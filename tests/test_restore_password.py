import allure
from pages.login_page import LoginPage
from pages.restore_page import RestorePasswordPage
from locators.login_locators import LoginLocators
from locators.restore_locators import RestoreLocators as RL


class TestRestorePassword:

    @allure.title('Проверка открытия страницы "Восстановление пароля"')
    def test_restore_page_open(self, driver):
        lp = LoginPage(driver)
        lp.open_login_page()
        lp.click_element_if_clickable(LoginLocators.RESTORE_PASSWORD_BUTTON)
        rp = RestorePasswordPage(driver)
        assert rp.title_check() is True, 'Страница восстановления пароля не открыта'

    @allure.title('Проверка ввода почты и нажатие на кнопку "Восстановить"')
    def test_input_data_and_click_restore_button(self, driver, test_data):
        rpp = RestorePasswordPage(driver)
        rpp.open_forgot_password_page()
        rpp.input_email(test_data)
        rpp.click_element_if_clickable(RL.RESTORE_BUTTON)
        assert rpp.exist_password_field_check() is True, ('После нажатия на кнопку "Восстановить" '
                                                          'не открылась страница смены пароля')

    @allure.step('Проверка статуса поля ввода "Пароль" после нажатия кнопки "Показать/скрыть"')
    def test_show_hide_button(self, driver, test_data):
        rpp = RestorePasswordPage(driver)
        rpp.precondition_for_show_hide_button(test_data)
        rpp.input_password(test_data)
        rpp.click_element_if_visible(RL.SHOW_HIDE_BUTTON)
        assert (rpp.stroke_password_field_check()
                is True and rpp.active_password_field_check() is True), ('Статус поля ввода "Пароль'
                                                                       'не '
                                                                       'соответствует '
                                                                       'ожидаемому')
