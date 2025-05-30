from selenium.webdriver.common.by import By


# Локаторы страницы авторизации - login_page.py
EMAIL = (By.NAME, "email")
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
PASSWORD = (By.NAME, "password")
PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

# Локаторы восстановления пароля - recover_page.py
RECOVER_BUTTON = (By.CLASS_NAME, "button_button__33qZ0")
PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[@href='/forgot-password']")
SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input_type_password')]//div[contains(@class, 'input__icon-action')]")
NEW_PASSWORD_INPUT = (By.NAME, "Введите новый пароль")

# Локаторы главной страницы - main_page.py
CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
ORDER_FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']")
MODAL = (By.CLASS_NAME, "Modal_modal__content__3vY0j")
MODAL_CLOSE = (By.CLASS_NAME, "Modal_modal__close__TnseK")
COUNTER = (By.CLASS_NAME, "counter_counter__ZNLkj")
ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
# Локаторы ингредиентов
INGREDIENT_MODAL = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")
INGREDIENT_MODAL_CLOSE_BUTTON = (By.CLASS_NAME, "Modal_modal__close__TnseK")
BASKET_LIST = (By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_")
INGREDIENT_ITEMS = (By.CSS_SELECTOR, "a[class*='BurgerIngredient_ingredient__']")

# Локаторы списка заказов - feed_page.py
ORDER_CARD = (By.CLASS_NAME, "OrderHistory_order__1VAmS")
TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за всё время:']/following-sibling::p")
TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
ORDER_MODAL = (By.CLASS_NAME, "Modal_modal__contentBox__sCy8X")
ORDER_MODAL_TITLE = (By.XPATH, "//p[contains(text(), 'идентификатор заказа')]")
ORDER_CARD = (By.CSS_SELECTOR, "a[class*='OrderHistory_link__']")
ORDER_NUMBER_IN_CARD = (By.CSS_SELECTOR, "p.text.text_type_digits-default")
DONE_TOTAL = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
DONE_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
ORDER_FEED_LIST = (By.XPATH, "//*[@id='root']/div/main/div/div/ul")
ORDER_IN_FEED_BY_NUMBER = lambda number: (By.XPATH, f"//p[text()='#0{number}']")
ORDER_FEED_DONE_TOTAL = (By.CLASS_NAME, "OrderFeed_number__2MbrQ")
ORDER_FEED_DONE_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
ORDER_FEED_IN_PROGRESS = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi > li")
ORDER_FEED_IN_PROGRESS_LIST = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem li")
ORDER_MODAL_BOX = (By.CLASS_NAME, "Modal_orderBox__1xWdi")

def ingredient_by_name(name):
    return (By.XPATH, f"//p[text()='{name}']/ancestor::a")

# Локатор для входа в личный кабинет - PROFILE_LINK
# Локаторы профиля - profile_page.py
PROFILE_LINK = (By.CSS_SELECTOR, "a[href='/account']")
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
