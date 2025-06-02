from Diplom_33.locators.locators import EMAIL_INPUT, PASSWORD_INPUT, LOGIN_BUTTON, PASSWORD_RECOVERY_LINK
from Diplom_33.pages.base_page import BasePage
import time

class LoginPage(BasePage):
    def login(self, email, password):
        self.fill(EMAIL_INPUT, email)
        self.fill(PASSWORD_INPUT, password)
        self.wait_clickable(LOGIN_BUTTON)
        self.click(LOGIN_BUTTON)
        time.sleep(3)
        print("Текущий URL:", self.get_current_url())

    def go_to_password_recovery(self):
        self.click(PASSWORD_RECOVERY_LINK)
