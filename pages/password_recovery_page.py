from selenium.webdriver.common.by import By
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.locators import PROFILE_LINK, PASSWORD_RECOVERY_LINK, EMAIL_INPUT, RECOVER_BUTTON, SHOW_PASSWORD_BUTTON, NEW_PASSWORD_INPUT
from Diplom_3.pages.profile_page import ProfilePage
from selenium.common.exceptions import NoSuchElementException
from Diplom_3.locators.locators import INGREDIENT_MODAL_CLOSE_BUTTON

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
        element = self.get_element_property(NEW_PASSWORD_INPUT, "value")
        return element == expected_value

    def close_overlay_if_exists(self):
        potential_classes = [
            "Modal_modal_overlay__x2ZCr",  # Firefox
            "Modal_modal__overlay__3U0G9",  # Chrome
            "Modal_modal__overlay__3vY0j",  # на всякий
        ]
        for cls in potential_classes:
            try:
                overlays = self.get_elements((By.CLASS_NAME, cls))
                for overlay in overlays:
                    if overlay.is_displayed():
                        self.click(INGREDIENT_MODAL_CLOSE_BUTTON)
                        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, cls)))
            except Exception:
                pass