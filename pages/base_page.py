import allure
from selenium.webdriver import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data import data_tests
from locators.profile_locators import ProfileLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, email, password):
        self.visibility_of_element(ProfileLocators.LOGIN_EMAIL).send_keys(email)
        self.visibility_of_element(ProfileLocators.LOGIN_PASSWORD).send_keys(password)
        self.visibility_of_element(ProfileLocators.LOGIN_BUTTON).click()

    @allure.description('Получить текущий урл')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Получить текст')
    def get_text(self, locator):
        actually_text = self.driver.find_element(*locator).text
        return actually_text

    @allure.description('Найти элемент и кликнуть по нему')
    def find_element_and_click(self, locator):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))
        return self.find_element_on_page(locator).click()

    @allure.description('Найти элемент на странице')
    def find_element_on_page(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))

    @allure.description('Найти элемент и кликнуть по нему')
    def find_element_and_click(self, locator):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))
        return self.find_element_on_page(locator).click()

    @allure.description("Ожидание кликабельного элемента на странице")
    def wait_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))

    @allure.description("Ожидание видимости элемента на странице")
    def visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))

    def wait_url_changing(self):
        initial_url = self.driver.current_url
        return WebDriverWait(self.driver, 10).until(ec.url_changes(initial_url))

    def wait_expected_url(self, expected_url: str):
        return WebDriverWait(self.driver, 10).until(ec.url_to_be(expected_url))

    @allure.description('Переместиться к элементу и кликнуть')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.description('Перетащить элемент')
    def drag_and_drop_to_element(self, from_locator, to_locator):
        draggable = self.driver.find_element(*from_locator)
        droppable = self.driver.find_element(*to_locator)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()

    @allure.step("Найти все элементы")
    def find_all_elements(self, locator):
        return WebDriverWait(self.driver, 20).until(ec.presence_of_all_elements_located(locator))




