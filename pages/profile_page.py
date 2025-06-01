from Diplom_33.locators.locators import PROFILE_LINK, ORDER_HISTORY_LINK, LOGOUT_BUTTON, INGREDIENT_MODAL_CLOSE_BUTTON, MODAL_OVERLAYS
from Diplom_33.pages.base_page import BasePage

class ProfilePage(BasePage):
    def go_to_profile(self):
        self.close_overlay_if_exists()
        self.wait_visible(PROFILE_LINK)
        self.click(PROFILE_LINK)
        self.wait.until(EC.url_contains('/account/profile'))

    def go_to_order_history(self):
        self.wait_visible(ORDER_HISTORY_LINK)
        self.click(ORDER_HISTORY_LINK)

    def open_order_history(self):
        self.go_to_order_history()

    def logout(self):
        self.click(LOGOUT_BUTTON)

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

    def get_current_url(self):
        return self.driver.current_url
