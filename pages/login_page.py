from Diplom_33.locators.locators import EMAIL, PASSWORD, LOGIN_BUTTON, PASSWORD_RECOVERY_LINK, EMAIL_INPUT, PASSWORD_INPUT
from Diplom_33.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def login(self, email, password):
        self.fill(EMAIL_INPUT, email)
        self.fill(PASSWORD_INPUT, password)
        # Ждем, пока кнопка станет кликабельной после ввода пароля
        self.wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))
        self.click(LOGIN_BUTTON)

    def go_to_password_recovery(self):
        self.click(PASSWORD_RECOVERY_LINK)