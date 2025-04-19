import allure

from conftest import *
from data.urls import Urls

class TestProfile:

    @allure.title('Переход по клику на «Личный кабинет»,')
    def test_check_click_account_profile(self, page_profile):
        page_profile.click_on_profile()
        page_profile.wait_expected_url(Urls.ACCOUNT_PROFILE)
        assert page_profile.get_current_url() == Urls.ACCOUNT_PROFILE

    @allure.title('Переход по клику на «История заказов»,')
    def test_click_on_history_orders(self, page_profile):
        page_profile.click_on_profile()
        page_profile.click_on_history()
        assert page_profile.get_current_url() == Urls.HISTORY_ORDERS

    # Не проходит в фаерфокс
    @allure.title('Выход из ЛК')
    def test_click_on_history_orders(self, page_profile):
        page_profile.click_on_profile()
        page_profile.click_on_exit()
        current_url = page_profile.find_header_login()
        assert current_url == Urls.LOGIN
