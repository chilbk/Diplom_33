from Diplom_3.locators.locators import PROFILE_LINK, ORDER_HISTORY_LINK, LOGOUT_BUTTON, INGREDIENT_MODAL_CLOSE_BUTTON, MODAL, MODAL_CLOSE
from Diplom_3.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class ProfilePage(BasePage):
    def go_to_profile(self):
        self.close_overlay_if_exists()
        self.wait_for_element_to_be_visible(PROFILE_LINK)
        self.click(PROFILE_LINK)

    def go_to_order_history(self):
        self.wait_for_element_to_be_visible(ORDER_HISTORY_LINK)
        self.click(ORDER_HISTORY_LINK)

    def open_order_history(self):
        self.go_to_order_history()

    def logout(self):
        self.click(LOGOUT_BUTTON)

    def close_overlay_if_exists(self):
        potential_classes = [
            "Modal_modal_overlay__x2ZCr",  # Firefox
            "Modal_modal__overlay__3U0G9",  # Chrome
            "Modal_modal__overlay__3vY0j",  # Запасной
        ]

        for class_name in potential_classes:
            try:
                overlay_locator = (By.CLASS_NAME, class_name)
                # Ждём появления (если не появится — окей)
                WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located(overlay_locator)
                )
                # Ждём пока исчезнет
                WebDriverWait(self.driver, 5).until(
                    EC.invisibility_of_element_located(overlay_locator)
                )
            except TimeoutException:
                pass  # если не появилось или не исчезло — просто продолжаем

    def get_current_url(self):
        return self.driver.current_url