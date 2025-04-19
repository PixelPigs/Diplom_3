from selenium import webdriver

# Создание драйверов под разные браузеры
class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == 'firefox':
            return webdriver.Firefox()
        elif browser_name == 'chrome':
            return webdriver.Chrome()
        else:
            raise ValueError(f"Браузер {browser_name} не поддерживается.")