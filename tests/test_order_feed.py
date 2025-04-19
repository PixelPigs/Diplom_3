import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from conftest import *
from data.urls import Urls
from locators.order_feed_locators import OrderFeedLocators
from locators.profile_locators import ProfileLocators


class TestOrderFeed:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_check_window(self, page_order_feed):
        page_order_feed.click_order_feed()
        page_order_feed.click_order()
        assert page_order_feed.window_of_order() == True

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_check_orders_history_in_orders_feed(self, page_order_feed):
        order_id = page_order_feed.make_order()
        page_order_feed.click_cross_order()
        page_order_feed.click_on_profile()
        page_order_feed.click_on_history()
        order_in_history = page_order_feed.order_id_in_history(order_id)
        page_order_feed.click_order_feed()
        order_id_in_feed = page_order_feed.order_id_in_feed(order_id)
        assert order_in_history == order_id_in_feed

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    @pytest.mark.parametrize('counter', [OrderFeedLocators.ALL_ORDER_COUNT, OrderFeedLocators.TODAY_ORDER_COUNT])
    def test_orders_counter_all_time(self, page_order_feed, counter):
        page_order_feed.click_order_feed()
        page_order_feed.visibility_of_element(OrderFeedLocators.ALL_ORDER_COUNT)
        actual_value_counter = page_order_feed.get_counter_value(counter)
        page_order_feed.click_constructor()
        page_order_feed.make_order()
        page_order_feed.click_cross_order()
        page_order_feed.click_order_feed()
        WebDriverWait(page_order_feed.driver, 10).until(ec.visibility_of_element_located(counter))
        current_value_counter = page_order_feed.get_counter_value(counter)
        assert int(current_value_counter) > int(actual_value_counter)

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_check_order_status(self, page_order_feed):
        order_id = page_order_feed.make_order()
        page_order_feed.click_cross_order()
        page_order_feed.click_order_feed()
        order_in_work = page_order_feed.get_order_in_work()
        assert int(order_id) == int(order_in_work)
