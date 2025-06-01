import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from Diplom_3.user_api_helper import register_user, delete_user
import allure
from allure_commons.types import AttachmentType
from Diplom_3.pages.main_page import MainPage
from Diplom_3.pages.login_page import LoginPage
from Diplom_3.pages.profile_page import ProfilePage
from Diplom_3.pages.password_recovery_page import PasswordRecoveryPage
from Diplom_3.locators.urls import BASE_URL, PROFILE_URL, HISTORY_URL, LOGIN_URL, RESET_PASSWORD_URL


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        options = ChromeOptions()
        # options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
        
        # Создаем временный профиль
        profile = FirefoxProfile()
        profile.set_preference("browser.startup.homepage", "about:blank")
        profile.set_preference("startup.homepage_welcome_url", "about:blank")
        profile.set_preference("startup.homepage_welcome_url.additional", "")
        profile.set_preference("browser.tabs.remote.autostart", False)
        profile.set_preference("browser.tabs.remote.autostart.1", False)
        profile.set_preference("browser.tabs.remote.autostart.2", False)
        
        options = FirefoxOptions()
        options.profile = profile
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError("Unsupported browser")
    yield driver
    driver.quit()

@pytest.fixture
def test_user():
    email = "vda_diplom@mail.ru"
    password = "qwerty123"
    name = "Diplom"
    access_token, refresh_token = register_user(email, password, name)
    yield {"email": email, "password": password, "access_token": access_token}
    delete_user(access_token)

@pytest.fixture
@allure.title("Фикстура для тестов профиля")
def profile_setup(driver, test_user):
    driver = driver
    main_page = MainPage(driver)
    main_page.open(BASE_URL)
    main_page.go_to_account()
    login_page = LoginPage(driver)
    login_page.login(test_user["email"], test_user["password"])
    profile_page = ProfilePage(driver)
    profile_page.close_overlay_if_exists()
    return {
        "driver": driver,
        "main_page": main_page,
        "login_page": login_page,
        "profile_page": profile_page
    }

@pytest.fixture
@allure.title("Фикстура для тестов авторизованного пользователя")
def logged_user_setup(driver, test_user):
    driver = driver
    page = MainPage(driver)
    page.open(BASE_URL)
    page.go_to_account()
    login_page = LoginPage(driver)
    login_page.login(test_user["email"], test_user["password"])
    return {
        "page": page,
        "login_page": login_page
    }

@pytest.fixture
@allure.title("Фикстура для тестов ленты заказов")
def feed_setup(main_setup):
    page = main_setup
    page.go_to_order_feed()
    feed_page = FeedPage(page.driver)
    return {
        "main_page": page,
        "feed_page": feed_page
    }

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open(BASE_URL)
    return page

@pytest.fixture
def recovery_page(driver):
    page = PasswordRecoveryPage(driver)
    page.open(RESET_PASSWORD_URL)
    return page