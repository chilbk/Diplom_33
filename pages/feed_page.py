from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.locators import ORDER_FEED_LIST, ORDER_MODAL_BOX, ORDER_CARD, ORDER_MODAL_TITLE, DONE_TOTAL, DONE_TODAY, ORDER_IN_FEED_BY_NUMBER, ORDER_FEED_DONE_TOTAL, ORDER_FEED_DONE_TODAY, ORDER_FEED_IN_PROGRESS_LIST
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FeedPage(BasePage):
    def open_first_order_in_feed(self):
        orders = self.get_elements(ORDER_CARD)
        if orders:
            self.wait.until(EC.element_to_be_clickable(orders[0])).click()

    def is_order_modal_box_visible(self):
        return self.is_visible(ORDER_MODAL_BOX)


        def get_total_orders_done(self):
            return int(self.get_text(ORDER_FEED_DONE_TOTAL))

