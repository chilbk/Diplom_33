
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from Diplom_33.pages.base_page import BasePage
from Diplom_33.locators.locators import (CONSTRUCTOR_LINK, ingredient_by_name, INGREDIENT_MODAL, INGREDIENT_MODAL_CLOSE_BUTTON,
                                        PROFILE_LINK, EMAIL_INPUT, ORDER_MODAL_TITLE, BASKET_LIST, ORDER_BUTTON, INGREDIENT_ITEMS, ORDER_FEED_LINK,
                                        MODAL_CLOSE_BUTTON, INGREDIENT_COUNTER, MODAL_OVERLAYS)
from selenium.webdriver.support import expected_conditions as EC
from Diplom_3.pages.profile_page import ProfilePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):
    def go_to_constructor(self):
            self.click(CONSTRUCTOR_LINK)

    def go_to_order_feed(self):
        try:
            self.wait.until(EC.element_to_be_clickable(ORDER_FEED_LINK))
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*ORDER_FEED_LINK))
            return True
        except Exception as e:
            print(f"Ошибка при переходе в ленту заказов: {e}")
            return False

    def open_ingredient_modal(self, name):
        try:
            ingredient_locator = ingredient_by_name(name)
            self.wait.until(EC.element_to_be_clickable(ingredient_locator))
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*ingredient_locator))
            return True
        except Exception as e:
            print(f"Ошибка при открытии модального окна ингредиента: {e}")
            return False

    def is_ingredient_modal_visible(self):
        return self.is_visible(INGREDIENT_MODAL)

    def is_ingredient_modal_hidden(self):
        try:
            modal = self.driver.find_element(*INGREDIENT_MODAL)
            is_hidden = not modal.is_displayed()

            # Дополнительно проверим через JS стиль display
            display_style = self.driver.execute_script("return window.getComputedStyle(arguments[0]).display;", modal)
            return is_hidden or display_style == "none"
        except:
            return True

    def close_modal(self):
        try:
            close_button = self.driver.find_element(*INGREDIENT_MODAL_CLOSE_BUTTON)
            self.driver.execute_script("arguments[0].click();", close_button)
            self.wait.until(EC.invisibility_of_element_located(INGREDIENT_MODAL))
        except Exception as e:
            print(f"Ошибка при закрытии модалки: {e}")

    def go_to_account(self):
        self.click(PROFILE_LINK)
        self.is_visible(EMAIL_INPUT)

# А вот этот drag and drop у меня не получилось через ActionChains выполнять
    # Пришлось попросить помощи, поэтому код выглядит тяжеловесным
    # Код выполнен с использованием JavaScript, т.к. Firefox не вывез ActionChains
    # И пускай мне помогли, но я поэтапно знаю что здесь происходит
    # Как понимаю, автотестеру, который работает с UI, без JS вообще никак
    def drag_ingredient_to_basket(self, name):
        source = self.wait.until(EC.presence_of_element_located(ingredient_by_name(name)))
        target = self.wait.until(EC.presence_of_element_located(BASKET_LIST))
        # Запускаем выполнение самого JS
        # const dataTransfer = new DataTransfer() - запускает события drag event
        # А вообще dataTransfer хранит данные, передаваемые при drag and drop
        # const dragStartEvent - начало перетаскивания
        # const dropEvent - имитация отпуска перетаскиваемого элемента
        # const dropEndEvent - конец перетаскивания

        # source.dispatchEvent(dragStartEvent)
        # target.dispatchEvent(dropEvent)           - Вот здесь программно отправляются события на элементы
        # source.dispatchEvent(dragEndEvent)

        self.driver.execute_script(""" 
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
        ingredient = self.wait.until(EC.visibility_of_element_located(ingredient_by_name(name)))
        try:
            return ingredient.find_element(*ingredient_by_name(name)).text
        except:
            return "0"

    def place_order(self):
        try:
            for overlay_locator in MODAL_OVERLAYS:
                overlays = self.driver.find_elements(*overlay_locator)
                for overlay in overlays:
                    if overlay.is_displayed():
                        try:
                            close_button = self.driver.find_element(*MODAL_CLOSE_BUTTON)
                            self.driver.execute_script("arguments[0].click();", close_button)
                            self.wait.until(EC.invisibility_of_element_located(overlay_locator))
                        except Exception:
                            pass
        except Exception:
            pass

        # Вот тут ждем, пока исчезнет вообще всё, что только могло отображаться
        WebDriverWait(self.driver, 10).until(
            lambda d: all(
                not o.is_displayed() for cls in overlay_selectors for o in d.find_elements(By.CLASS_NAME, cls))
        )


        self.click(ORDER_BUTTON)

    def is_order_confirmation_visible(self):
        return self.is_visible(ORDER_MODAL_TITLE)

    def get_ingredient_counter_text(self, name):
        ingredient = self.driver.find_element(*ingredient_by_name(name))
        return ingredient.find_element(*INGREDIENT_COUNTER).text

    def place_sample_order_and_get_number(self):
        ingredient = self.driver.find_elements(*INGREDIENT_ITEMS)[0]
        target = self.driver.find_element(*BASKET_LIST)
        self.driver.execute_script("""
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
                overlays = self.driver.find_elements(*overlay_locator)
                for overlay in overlays:
                    if overlay.is_displayed():
                        self.driver.find_element(*INGREDIENT_MODAL_CLOSE_BUTTON).click()
                        self.wait.until(EC.invisibility_of_element_located(overlay_locator))
            except Exception:
                pass