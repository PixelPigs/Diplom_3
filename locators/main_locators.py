from selenium.webdriver.common.by import By


class MainLocators:
    # Конструктор
    BUTTON_CONSTRUCTOR = By.PARTIAL_LINK_TEXT, "Конструктор"
    BURGER_TITLE = By.XPATH, ".//section[1]/h1[text()='Соберите бургер']"
    BUN_INGREDIENT = By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]'
    DETAILS = By.XPATH, '//h2[text()="Детали ингредиента"]'
    CROSS_BUTTON = By.XPATH, '//button[contains(@class,"close")]'
    CONSTRUCTOR_BASKET = By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']"
    # Лента заказов
    BUTTON_ORDER_FEED = By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li'
    COUNTER = By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]'
    # Заказ
    ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    ORDER_NUMBER = By.XPATH, '//p[text()="идентификатор заказа"]'