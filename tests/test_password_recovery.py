import pytest
import allure
from Diplom_33.pages.password_recovery_page import PasswordRecoveryPage
from Diplom_33.locators.urls import RESET_PASSWORD_URL
from Diplom_33.locators.locators import NEW_PASSWORD_INPUT

@allure.suite("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title("Тест навигации на страницу восстановления пароля")
    def test_navigate_to_recovery_page(self, recovery_page):
        with allure.step("Проверка нахождения на странице восстановления"):
            assert recovery_page.is_on_recovery_page(), "Не удалось перейти на страницу восстановления пароля"

    @allure.title("Тест ввода email для восстановления пароля")
    def test_fill_recovery_email(self, recovery_page):
        with allure.step("Ввод email для восстановления"):
            recovery_page.fill_email("vda_diplom@mail.ru")

        with allure.step("Отправка формы восстановления"):
            recovery_page.submit()

        with allure.step("Проверка успешной отправки формы"):
            assert recovery_page.email_was_submitted(), "Форма восстановления не была отправлена успешно"

    @allure.title("Тест ввода нового пароля")
    def test_password_input_highlight(self, recovery_page):
        with allure.step("Ввод email для восстановления"):
            recovery_page.fill_email("vda_diplom@mail.ru")
        with allure.step("Отправка формы восстановления"):
            recovery_page.submit()
        with allure.step("Проверка успешной отправки формы"):
            assert recovery_page.email_was_submitted(), "Форма восстановления не была отправлена успешно"
        with allure.step("Ввод нового пароля"):
            recovery_page.fill_new_password("password123")
        with allure.step("Проверка видимости поля ввода пароля"):
            assert recovery_page.is_visible(NEW_PASSWORD_INPUT), "Поле ввода нового пароля не видно"
        with allure.step("Отображение пароля"):
            recovery_page.show_password_field()
        with allure.step("Проверка значения пароля"):
            assert recovery_page.password_field_value_is("password123"), "Значение пароля не соответствует ожидаемому"