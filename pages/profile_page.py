import allure
from locators.profile_locators import ProfileLocators
from pages.base_page import BasePage

class ProfilePage(BasePage):

    @allure.step('Нажать на Личный кабинет')
    def click_on_profile(self):
        self.wait_element_to_be_clickable(ProfileLocators.BUTTON_ACCOUNT_PROFILE).click()

    @allure.step('Нажать на История заказов')
    def click_on_history(self):
        self.wait_element_to_be_clickable(ProfileLocators.BUTTON_HISTORY_ORDERS).click()

    @allure.step('Нажать на Выйти')
    def click_on_exit(self):
        self.find_element_and_click(ProfileLocators.BUTTON_EXIT)

    @allure.step('Найти заголовок Выйти и получить текущий урл')
    def find_header_login(self):
        self.visibility_of_element(ProfileLocators.LOGIN_TEXT)
        return self.get_current_url()
