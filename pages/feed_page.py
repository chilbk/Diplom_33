from Diplom_33.pages.base_page import BasePage
from Diplom_33.locators.locators import ORDER_CARD, ORDER_MODAL_BOX, ORDER_FEED_DONE_TOTAL

class FeedPage(BasePage):
    def open_first_order_in_feed(self):
        orders = self.get_elements(ORDER_CARD)
        if orders:
            self.wait_clickable(ORDER_CARD)
            self.js_click(ORDER_CARD)

    def is_order_modal_box_visible(self):
        return self.is_visible(ORDER_MODAL_BOX)

    def get_total_orders_done(self):
        return int(self.get_text(ORDER_FEED_DONE_TOTAL))
