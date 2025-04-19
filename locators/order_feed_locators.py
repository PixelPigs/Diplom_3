from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Лента заказов
    ORDER_IN_FEED = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'
    COMPOUND_ORDER = By.XPATH, '//p[text()="Cостав"]'
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")

    CROSS_ORDER = By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]"
    ORDERS_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, "
                                       "'text_type_digits-default')]")
    ORDERS_FEED = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                                    "text_type_digits-default']")

    ALL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    NUMBER_ORDER = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem "
                                    "OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")
    NUMBER_IN_WORK = (By.CSS_SELECTOR, 'ul[class^="OrderFeed_orderListReady"] li[class*="text_type_digits-default"]')
