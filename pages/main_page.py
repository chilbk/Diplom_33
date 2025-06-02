from Diplom_33.pages.base_page import BasePage
from Diplom_33.locators.locators import (CONSTRUCTOR_LINK, ingredient_by_name, INGREDIENT_MODAL, INGREDIENT_MODAL_CLOSE_BUTTON,
                                        PROFILE_LINK, EMAIL_INPUT, ORDER_MODAL_TITLE, BASKET_LIST, ORDER_BUTTON, INGREDIENT_ITEMS, ORDER_FEED_LINK,
                                        MODAL_CLOSE_BUTTON, INGREDIENT_COUNTER, MODAL_OVERLAYS)
import time
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def go_to_constructor(self):
        self.click(CONSTRUCTOR_LINK)

    def go_to_order_feed(self):
        try:
            self.wait_clickable(ORDER_FEED_LINK)
            self.js_click(ORDER_FEED_LINK)
            return True
        except Exception as e:
            print(f"Ошибка при переходе в ленту заказов: {e}")
            return False

    def open_ingredient_modal(self, name):
        try:
            ingredient_locator = ingredient_by_name(name)
            self.wait_clickable(ingredient_locator)
            self.js_click(ingredient_locator)
            return True
        except Exception as e:
            print(f"Ошибка при открытии модального окна ингредиента: {e}")
            return False

    def is_ingredient_modal_visible(self):
        return self.is_visible(INGREDIENT_MODAL)

    def is_ingredient_modal_hidden(self):
        try:
            modal = self.find(INGREDIENT_MODAL)
            is_hidden = not modal.is_displayed()
            display_style = self.get_display_style(INGREDIENT_MODAL)
            return is_hidden or display_style == "none"
        except:
            return True

    def close_modal(self):
        try:
            close_button = self.find(INGREDIENT_MODAL_CLOSE_BUTTON)
            self.execute_script("arguments[0].click();", close_button)
            self.wait_invisible(INGREDIENT_MODAL)
        except Exception as e:
            print(f"Ошибка при закрытии модалки: {e}")

    def go_to_account(self):
        self.click(PROFILE_LINK)
        self.is_visible(EMAIL_INPUT)

    def drag_ingredient_to_basket(self, name):
        source = self.wait_for_element(ingredient_by_name(name))
        target = self.wait_for_element(BASKET_LIST)
        self.execute_script(""" 
            function triggerDragAndDrop(source, target) {
                const dataTransfer = new DataTransfer(); 

                const dragStartEvent = new DragEvent('dragstart', {
                    dataTransfer: dataTransfer,
                    bubbles: true,
                    cancelable: true
                });

                const dropEvent = new DragEvent('drop', {
                    dataTransfer: dataTransfer,
                    bubbles: true,
                    cancelable: true
                });

                const dragEndEvent = new DragEvent('dragend', {
                    dataTransfer: dataTransfer,
                    bubbles: true,
                    cancelable: true
                });

                source.dispatchEvent(dragStartEvent);
                target.dispatchEvent(dropEvent);
                source.dispatchEvent(dragEndEvent);
            }

            triggerDragAndDrop(arguments[0], arguments[1]);
        """, source, target)

    def get_ingredient_counter_text(self, name):
        ingredient = self.wait_visible(ingredient_by_name(name))
        try:
            return ingredient.find_element(*INGREDIENT_COUNTER).text
        except:
            return "0"

    def place_order(self):
        try:
            for overlay_locator in MODAL_OVERLAYS:
                overlays = self.find_elements(overlay_locator)
                for overlay in overlays:
                    if overlay.is_displayed():
                        try:
                            close_button = self.find(MODAL_CLOSE_BUTTON)
                            self.execute_script("arguments[0].click();", close_button)
                            self.wait_invisible(overlay_locator)
                        except Exception:
                            pass
        except Exception:
            pass

        self.click(ORDER_BUTTON)

    def is_order_confirmation_visible(self):
        return self.is_visible(ORDER_MODAL_TITLE)

    def place_sample_order_and_get_number(self):
        ingredient = self.get_elements(INGREDIENT_ITEMS)[0]
        target = self.find(BASKET_LIST)
        self.execute_script("""
            const dataTransfer = new DataTransfer();
            arguments[0].dispatchEvent(new DragEvent('dragstart', {dataTransfer}));
            arguments[1].dispatchEvent(new DragEvent('drop', {dataTransfer}));
            arguments[0].dispatchEvent(new DragEvent('dragend', {dataTransfer}));
        """, ingredient, target)
        self.place_order()
        number = self.get_text(ORDER_MODAL_TITLE).strip("#")
        time.sleep(1)
        self.close_modal()
        return number

    def close_overlay_if_exists(self):
        for overlay_locator in MODAL_OVERLAYS:
            try:
                overlays = self.find_elements(overlay_locator)
                for overlay in overlays:
                    if overlay.is_displayed():
                        self.find(INGREDIENT_MODAL_CLOSE_BUTTON).click()
                        self.wait_invisible(overlay_locator)
            except Exception:
                pass
