from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)  # Увеличиваем таймаут до 30 секунд
        self.actions = ActionChains(driver)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait_clickable(locator).click()

    def fill(self, locator, value):
        field = self.wait_visible(locator)
        field.clear()
        field.send_keys(value)

    def is_visible(self, locator):
        return self.wait_visible(locator)

    def is_not_visible(self, locator):
        return self.wait.until_not(EC.visibility_of_element_located(locator))

    def get_text(self, locator):
        return self.wait_visible(locator).text

    def is_element_present(self, locator):
        try:
            self.find(locator)
            return True
        except NoSuchElementException:
            return False

    def get_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def get_element_property(self, locator, property_name):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_property(property_name)

    def hover(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.actions.move_to_element(element).perform()

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_url_contains(self, url_part, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: url_part in d.current_url
        )

    def get_current_url(self):
        return self.driver.current_url

    def get_page_source(self):
        return self.driver.page_source

    def find(self, locator):
        return self.driver.find_element(*locator)

    def js_click(self, locator):
        element = self.find(locator)
        self.execute_script("arguments[0].click();", element)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_display_style(self, locator):
        element = self.find(locator)
        return self.execute_script("return window.getComputedStyle(arguments[0]).display;", element)

    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False
