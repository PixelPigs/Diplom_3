import allure

from conftest import *
from data.data_tests import Users, Order
from data.urls import Urls
from locators.main_locators import MainLocators


class TestMainPage:

    @allure.description('Переход по клику на «Конструктор»')
    def test_click_constructor(self, page_main):
        page_main.click_constructor()
        assert page_main.visibility_of_element(MainLocators.BURGER_TITLE)

    @allure.description('Переход по клику на «Лента заказов»')
    def test_click_order_feed(self, page_main):
        page_main.click_order_feed()
        current_url = page_main.get_current_url()
        assert current_url == Urls.ORDER_FEED

    @allure.description('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_check_window(self, page_main):
        page_main.click_constructor()
        page_main.click_ingredient()
        assert page_main.find_element_on_page(MainLocators.DETAILS)

    @allure.description('Всплывающее окно закрывается кликом по крестику')
    def test_click_on_cross(self, page_main):
        page_main.click_constructor()
        page_main.click_ingredient()
        page_main.move_to_element_and_click(MainLocators.CROSS_BUTTON)
        assert page_main.visibility_of_element(MainLocators.BURGER_TITLE)

    # Не проходит в фаерфокс
    @allure.description('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_check_ingredient_counter(self, page_main):
        counter_value = page_main.get_counter_value()
        page_main.add_filling_to_order()
        actual_value = page_main.get_counter_value()
        assert actual_value > counter_value

    @allure.description('Заказ авторизованным пользователем')
    def test_check_order_auth(self, page_main):
        page_main.add_filling_to_order()
        page_main.click_order_button()
        actual_text = page_main.get_order_number()
        assert actual_text == Order.text_order
