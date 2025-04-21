import allure

from locators.main_locators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Нажать на кнопку Конструктор')
    def click_constructor(self):
        self.find_element_and_click(MainLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Нажать на кнопку Лента заказов')
    def click_order_feed(self):
        self.find_element_and_click(MainLocators.BUTTON_ORDER_FEED)

    @allure.step('Нажать на Ингредиент')
    def click_ingredient(self):
        self.find_element_and_click(MainLocators.BUN_INGREDIENT)

    @allure.step('Получаем значение каунтера')
    def get_counter_value(self):
        return self.get_text(MainLocators.COUNTER)

    @allure.step('Добавить ингредиент')
    def add_filling_to_order(self):
        self.wait_element_to_be_clickable(MainLocators.BUN_INGREDIENT)
        self.drag_and_drop_to_element(MainLocators.BUN_INGREDIENT, MainLocators.CONSTRUCTOR_BASKET)

    @allure.step('Нажать на кнопку Оформить заказ')
    def click_order_button(self):
        self.move_to_element_and_click(MainLocators.ORDER_BUTTON)

    @allure.step('Проверяем, что заказ оформлен')
    def get_order_number(self):
        self.visibility_of_element(MainLocators.ORDER_NUMBER)
        return self.get_text(MainLocators.ORDER_NUMBER)

