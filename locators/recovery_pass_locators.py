from selenium.webdriver.common.by import By


class RecoveryLocators:
    # Восстановление пароля
    RECOVERY_PASS = By.XPATH, ".//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']"
    TITLE_RECOVERY = "//h2[text()='Восстановление пароля']"
    RECOVERY_BUTTON = By.XPATH, ".//button[text()='Восстановить']"
    EMAIL_RECOVERY = By.XPATH, ".//input[@type='text' and @name='name']"
    EYE_BUTTON = By.XPATH, './/div[@class="input__icon input__icon-action"]'
    FIELD_PASS_ACTIVE = By.CSS_SELECTOR, '.input.input_status_active'
