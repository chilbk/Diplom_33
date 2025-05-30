from Diplom_33.locators.locators import PROFILE_LINK, ORDER_HISTORY_LINK, LOGOUT_BUTTON, INGREDIENT_MODAL_CLOSE_BUTTON, MODAL, MODAL_CLOSE
from Diplom_33.pages.base_page import BasePage
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
        for overlay_locator in MODAL_OVERLAYS:
            try:
                overlays = self.driver.find_elements(*overlay_locator)
                for overlay in overlays:
                    if overlay.is_displayed():
                        self.driver.find_element(*INGREDIENT_MODAL_CLOSE_BUTTON).click()
                        self.wait.until(EC.invisibility_of_element_located(overlay_locator))
            except Exception:
                pass

    def get_current_url(self):
        return self.driver.current_url