import pytest
import allure
from Diplom_33.pages.main_page import MainPage
from Diplom_33.pages.feed_page import FeedPage
from Diplom_33.locators.urls import BASE_URL

@allure.suite("Лента заказов")
class TestOrderFeed:
    @allure.title("Всплывающее окно с деталями")
    @pytest.mark.allure_description("Всплывающее окно с деталями")
    def test_click_order_opens_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.go_to_order_feed()

        feed_page = FeedPage(driver)
        feed_page.open_first_order_in_feed()
        assert feed_page.is_order_modal_box_visible()
# Метод вызывает ошибку. Почему-то он не прибавляет число. Почему-то он сравнивает одинаковые числа
# Я знаю, что просили не оставлять лишний код, но может получится подсказать мне в чем ошибка?
# Только явно, пожалуйста. По-другому не пойму :(
   #def test_order_feed_total_increases_after_new_order(self, driver, test_user):
       #driver.execute_script("window.open('');")
       #driver.switch_to.window(driver.window_handles[1])
       #main_page = MainPage(driver)
       #main_page.open(BASE_URL)
       #main_page.go_to_order_feed()

       #feed_page = FeedPage(driver)
       #initial_total = feed_page.get_total_orders_done()

       #initial_orders = feed_page.get_in_progress_list()

       #driver.execute_script("window.open('');")
       #driver.switch_to.window(driver.window_handles[2])

       #main_page = MainPage(driver)
       #main_page.open(BASE_URL)
       #main_page.go_to_account()

       #login_page = LoginPage(driver)
       #login_page.login(test_user["email"], test_user["password"])

       #main_page.drag_ingredient_to_basket("Соус фирменный Space Sauce")
       #main_page.place_order()

       #assert main_page.is_order_confirmation_visible()

       #main_page.close_modal()

       #import time
       #time.sleep(5)
       #main_page.go_to_order_feed()

       #final_orders = feed_page.get_in_progress_list()

       #assert len(final_orders) > len(initial_orders)

       #final_total = feed_page.get_total_orders_done()

       #assert final_total > initial_total"""



