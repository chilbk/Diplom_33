import pytest
import allure
from Diplom_33.pages.profile_page import ProfilePage
from Diplom_33.locators.urls import PROFILE_URL, HISTORY_URL, LOGIN_URL

@allure.suite("Профиль")
class TestProfile:

    @allure.title("Переход по клику на Личный кабинет")
    @pytest.mark.usefixtures("profile_setup")
    def test_go_to_profile_from_main(self, profile_setup):
        with allure.step("Ожидание закрытия модального окна"):
            profile_setup["profile_page"].close_overlay_if_exists()

        with allure.step("Переход в профиль"):
            profile_setup["profile_page"].go_to_profile()

    @allure.title("Переход к истории заказов")
    @pytest.mark.usefixtures("profile_setup")
    def test_open_order_history(self, profile_setup):
        with allure.step("Переход в профиль"):
            profile_setup["profile_page"].go_to_profile()

        with allure.step("Открытие истории заказов"):
            profile_setup["profile_page"].open_order_history()
            profile_setup["profile_page"].go_to_profile()

        with allure.step("Переход к истории заказов"):
            profile_setup["profile_page"].close_overlay_if_exists()
            profile_setup["profile_page"].go_to_order_history()

        with allure.step("Проверка URL истории заказов"):
            assert profile_setup["driver"].current_url == HISTORY_URL

    @allure.title("Выход из профиля")
    @pytest.mark.usefixtures("profile_setup")
    def test_logout(self, profile_setup):
        with allure.step("Переход в профиль"):
            profile_setup["profile_page"].go_to_profile()

        with allure.step("Выход из системы"):
            profile_setup["profile_page"].logout()

        with allure.step("Проверка URL после выхода"):
            profile_setup["profile_page"].wait_for_url_to_contain(LOGIN_URL)
            assert profile_setup["driver"].current_url == LOGIN_URL

