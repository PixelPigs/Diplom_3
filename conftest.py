import pytest
import time

from data.data_tests import Users
from data.urls import Urls
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.password_recovery_page import PasswordRecovery
from pages.profile_page import ProfilePage
from webdriver_factory import WebdriverFactory


# Фикстура: Переход к странице Восстановление пароля
@pytest.fixture(params=["chrome", "firefox"], scope="function")
def page_recovery_pass(request):
    browser_name = request.param
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.get(Urls.LOGIN)
    page_recovery_pass = PasswordRecovery(driver)
    yield page_recovery_pass
    driver.quit()

# Фикстура: Профиль
@pytest.fixture(params=["chrome", "firefox"], scope="function")
def page_profile(request):
    browser_name = request.param
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.get(Urls.LOGIN)
    page_profile = ProfilePage(driver)
    page_profile.authorization(Users.email, Users.password)
    time.sleep(3)
    yield page_profile
    driver.quit()

# Фикстура: Профиль
@pytest.fixture(params=["chrome", "firefox"], scope="function")
def page_main(request):
    browser_name = request.param
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.get(Urls.LOGIN)
    page_main = MainPage(driver)
    page_main.authorization(Users.email, Users.password)
    time.sleep(3)
    yield page_main
    driver.quit()

# Фикстура: Профиль
@pytest.fixture(params=["chrome", "firefox"], scope="function")
def page_order_feed(request):
    browser_name = request.param
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.get(Urls.LOGIN)
    page_order_feed = OrderFeedPage(driver)
    page_order_feed.authorization(Users.email, Users.password)
    time.sleep(3)
    yield page_order_feed
    driver.quit()

