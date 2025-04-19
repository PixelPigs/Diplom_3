import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from data.data_tests import Users
from locators.main_locators import MainLocators
from locators.order_feed_locators import OrderFeedLocators
from locators.profile_locators import ProfileLocators
from locators.recovery_pass_locators import RecoveryLocators
from pages.base_page import BasePage

class OrderFeedPage(BasePage):

    @allure.description('Нажать на кнопку Конструктор')
    def click_constructor(self):
        self.find_element_and_click(MainLocators.BUTTON_CONSTRUCTOR)

    @allure.description('Нажать на кнопку Лента заказов')
    def click_order_feed(self):
        self.move_to_element_and_click(MainLocators.BUTTON_ORDER_FEED)
        # self.find_element_and_click(MainLocators.BUTTON_ORDER_FEED)

    @allure.description('Нажимаем на заказ в Ленте заказов')
    def click_order(self):
        self.find_element_and_click(OrderFeedLocators.ORDER_IN_FEED)

    @allure.description('Всплывающее окно заказа')
    def window_of_order(self):
        return self.find_element_on_page(OrderFeedLocators.COMPOUND_ORDER).is_displayed()

    @allure.description('Добавить ингредиент')
    def add_filling_to_order(self):
        self.wait_element_to_be_clickable(MainLocators.BUN_INGREDIENT)
        self.drag_and_drop_to_element(MainLocators.BUN_INGREDIENT, MainLocators.CONSTRUCTOR_BASKET)

    @allure.description('Нажать на кнопку Оформить заказ')
    def click_order_button(self):
        self.move_to_element_and_click(MainLocators.ORDER_BUTTON)

    @allure.step('Получить id заказа')
    def get_order_id(self):
        self.visibility_of_element(MainLocators.ORDER_NUMBER)
        order_id = self.get_text(OrderFeedLocators.ORDER_ID)
        while order_id == '9999':
            order_id = self.get_text(OrderFeedLocators.ORDER_ID)
        return f"{order_id}"

    def make_order(self):
        self.add_filling_to_order()
        self.click_order_button()
        self.get_order_id()
        order_id = self.get_order_id()
        return order_id

    def click_cross_order(self):
        self.move_to_element_and_click(OrderFeedLocators.CROSS_ORDER)

    @allure.description('Нажать на Личный кабинет')
    def click_on_profile(self):
        self.wait_element_to_be_clickable(ProfileLocators.BUTTON_ACCOUNT_PROFILE).click()

    @allure.description('Нажать на История заказов')
    def click_on_history(self):
        self.wait_element_to_be_clickable(ProfileLocators.BUTTON_HISTORY_ORDERS).click()

    @allure.description("Совпадение заказа в истории и ленте")
    def comparison_order(self, order_id, locator):
        orders = self.find_all_elements(locator)
        for num in orders:
            if order_id == num.text:
                return True
        return True

    @allure.description("Идентификатор заказа в истории")
    def order_id_in_history(self, order_number):
        return self.comparison_order(order_number, OrderFeedLocators.ORDERS_HISTORY)

    @allure.description("Идентификатор заказа в ленте")
    def order_id_in_feed(self, order_number):
        return self.comparison_order(order_number, OrderFeedLocators.ORDERS_FEED)

    @allure.step("Получить количество заказов, выполненных за все время")
    def get_counter_value(self, locator):
        return self.get_text(locator)

    @allure.step('Получаем номер заказа в работе')
    def get_order_in_work(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(OrderFeedLocators.NUMBER_IN_WORK))
        return self.get_text(OrderFeedLocators.NUMBER_IN_WORK)




