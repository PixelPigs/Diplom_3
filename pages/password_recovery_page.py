import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from data.data_tests import Users
from locators.recovery_pass_locators import RecoveryLocators
from pages.base_page import BasePage


class PasswordRecovery(BasePage):

    @allure.description('Ожидание, когда поле Пароль станет активным')
    def wait_active_pass(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(RecoveryLocators.FIELD_PASS_ACTIVE))

    @allure.description('Ожидание, когда Восстановить Пароль станет активным')
    def wait_active_recovery_pass(self):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(RecoveryLocators.RECOVERY_PASS))

    @allure.description('Ожидание и нажатие кнопки скрыть/показать пароль')
    def click_toggle_password_icon(self):
        return self.wait_element_to_be_clickable(RecoveryLocators.EYE_BUTTON).click()

    @allure.description('Нажать Восстановить')
    def recovery_password(self):
        self.wait_element_to_be_clickable(RecoveryLocators.RECOVERY_PASS).click()
        self.wait_element_to_be_clickable(RecoveryLocators.EMAIL_RECOVERY).send_keys(Users.email)
        self.wait_element_to_be_clickable(RecoveryLocators.RECOVERY_BUTTON).click()
