from selenium.webdriver.common.by import By

class ProfileLocators:
    # Вход в личный кабинет
    LOGIN_BUTTON = By.XPATH, ".//button[text()='Войти']"

    LOGIN_EMAIL = By.XPATH, ".//input[@type='text' and @name='name']"
    LOGIN_PASSWORD = By.XPATH, ".//input[@type='password' and @name='Пароль']"
    BUTTON_ACCOUNT_PROFILE = By.XPATH, ".//p[text()='Личный Кабинет']"
    MODAL_WINDOW = By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"
    MODAL_OVERLAY = By.CSS_SELECTOR, "[class^='Modal_modal_overlay']"
    BUTTON_HISTORY_ORDERS = By.LINK_TEXT, 'История заказов'
    BUTTON_EXIT = By.XPATH, ".//button[text()='Выход']"
    HEADER_LOGIN = By.XPATH, "//h2[text()='Вход']"
    BUTTON_ORDER = By.XPATH, ".//button[text()='Оформить заказ']"
    LOGIN_TEXT = (By.XPATH, ".//h2[text()='Вход']")

