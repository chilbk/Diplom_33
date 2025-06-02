from Diplom_33.pages.base_page import BasePage
from Diplom_33.locators.locators import (PROFILE_LINK, PASSWORD_RECOVERY_LINK, EMAIL_INPUT,
                                        RECOVER_BUTTON, SHOW_PASSWORD_BUTTON, NEW_PASSWORD_INPUT, MODAL_OVERLAYS, INGREDIENT_MODAL_CLOSE_BUTTON)

class PasswordRecoveryPage(BasePage):
    def go_to_recovery_page(self):
        self.click(PASSWORD_RECOVERY_LINK)

    def go_to_account(self):
        self.close_overlay_if_exists()
        self.click(PROFILE_LINK)

    def is_on_recovery_page(self):
        return self.is_visible(EMAIL_INPUT)

    def fill_email(self, email):
        self.fill(EMAIL_INPUT, email)

    def submit(self):
        self.click(RECOVER_BUTTON)

    def email_was_submitted(self):
        return self.is_visible(NEW_PASSWORD_INPUT)

    def show_password_field(self):
        self.click(SHOW_PASSWORD_BUTTON)

    def fill_new_password(self, password):
        self.fill(NEW_PASSWORD_INPUT, password)

    def password_field_value_is(self, expected_value):
        value = self.get_element_property(NEW_PASSWORD_INPUT, "value")
        return value == expected_value

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