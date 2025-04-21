import allure

from conftest import *
from data.data_tests import Users
from data.urls import Urls


class TestRecoveryPass:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_recovery_page(self, page_recovery_pass):
        page_recovery_pass.wait_active_recovery_pass().click()
        current_url = page_recovery_pass.get_current_url()
        assert current_url == Urls.RECOVERY_PASS

    @allure.title('Проверить страницу восстановления пароля, после введения почты')
    def test_input_email_click_recovery_button(self, page_recovery_pass):
        page_recovery_pass.recovery_password()
        page_recovery_pass.wait_url_changing()
        assert page_recovery_pass.get_current_url() == Urls.RESET_PASS

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_click_button_eye_highlights_field(self, page_recovery_pass):
        page_recovery_pass.recovery_password()
        page_recovery_pass.click_toggle_password_icon()
        assert page_recovery_pass.wait_active_pass()
