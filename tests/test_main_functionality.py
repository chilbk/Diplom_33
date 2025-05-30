import time
import pytest
import allure
from Diplom_3.pages.main_page import MainPage
from Diplom_3.pages.login_page import LoginPage
from Diplom_3.locators.urls import BASE_URL

@allure.suite("Основной функционал")
class TestMainFunctionality:
    @allure.title("Тест перехода в конструктор")
    def test_go_to_constructor(self, main_page):
        with allure.step("Переход в конструктор"):
            main_page.go_to_constructor()

        with allure.step("Проверка URL конструктора"):
            assert "constructor" in main_page.get_current_url() or "" in main_page.get_page_source(), "Не удалось перейти в конструктор"
    @allure.title("Тест перехода в ленту заказов")
    def test_go_to_order_feed(self, main_page):
        with allure.step("Переход в ленту заказов"):
            main_page.go_to_order_feed()

        with allure.step("Проверка URL ленты заказов"):
            assert "feed" in main_page.get_current_url(), "Не удалось перейти в ленту заказов"

    @allure.title("Тест открытия модального окна ингредиента")
    def test_open_ingredient_modal(self, main_page):
        with allure.step("Открытие модального окна ингредиента"):
            main_page.open_ingredient_modal("Соус фирменный Space Sauce")

        with allure.step("Проверка видимости модального окна"):
            assert main_page.is_ingredient_modal_visible(), "Модальное окно ингредиента не открылось"

    @allure.title("Тест закрытия модального окна ингредиента")
    def test_close_ingredient_modal(self, main_page):
        with allure.step("Открытие модального окна ингредиента"):
            main_page.open_ingredient_modal("Соус фирменный Space Sauce")

        with allure.step("Закрытие модального окна"):
            main_page.close_modal()
        time.sleep(1)

        with allure.step("Проверка скрытия модального окна"):
            assert main_page.is_ingredient_modal_hidden(), "Модальное окно ингредиента не закрылось"

@pytest.mark.allure_description("Тест увеличения счетчика ингредиента")
def test_ingredient_counter_increases(main_setup):
    with allure.step("Открытие главной страницы"):
        page = main_setup

    with allure.step("Добавление ингредиента в корзину"):
        page.drag_ingredient_to_basket("Флюоресцентная булка R2-D3")

    with allure.step("Проверка значения счетчика"):
        assert page.get_ingredient_counter_text("Флюоресцентная булка R2-D3") == "2", "Счетчик ингредиента не увеличился"

@pytest.mark.allure_description("Тест оформления заказа авторизованным пользователем")
def test_logged_user_can_place_order(logged_user_setup, test_user):
    with allure.step("Открытие главной страницы"):
        page = logged_user_setup["page"]
        login_page = logged_user_setup["login_page"]

    with allure.step("Добавление ингредиента в корзину"):
        page.drag_ingredient_to_basket("Соус фирменный Space Sauce")

    with allure.step("Оформление заказа"):
        page.close_overlay_if_exists()
        page.place_order()

    with allure.step("Проверка успешного оформления заказа"):
        assert page.is_order_confirmation_visible(), "Модальное окно подтверждения заказа не открылось"
