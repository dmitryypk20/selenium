from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    # Елементи на головній сторінці
    PRODUCT_ITEM = (By.CLASS_NAME, 'product-item')
    PRODUCT_LINK = (By.TAG_NAME, 'a')
    ADD_TO_CART_BUTTON = (By.XPATH, "//input[contains(@id, 'add-to-cart-button')]")
    PRODUCT_ADDED = (By.XPATH, "//p[contains(text(), 'The product has been added to your')]")

    def __init__(self, driver):
        super().__init__(driver)


    def open_page(self):
        self.driver.get(BASE_URL)


    def go_to_cart(self):
        self.driver.get(f'{BASE_URL}/cart')


    def go_to_category(self):
        self.driver.get(f'{BASE_URL}/books')

    def go_to_product(self):
        self.driver.get(f'{BASE_URL}/141-inch-laptop')

    def add_product_to_cart(self):
        WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((self.PRODUCT_ITEM))
            )

        # Шукаємо елементи
        products = self.driver.find_elements(*self.PRODUCT_ITEM)
        products_links = []
        print(f'Знайдено {len(products)} продуктів')

        for product in products:
            try:
                link = product.find_element(*self.PRODUCT_LINK).get_attribute('href')
                products_links.append(link)
            except Exception as e:
                print(f'Виникла помилка при пошуку посилання: {e}')

        print(f'Знайдено {len(products_links)} посилань')

        product_link = products_links[1]
        self.driver.get(product_link)
        # Перевірка чи є кнопка для кліка
        try:
            add_to_card_button = self.find_element(locator=self.ADD_TO_CART_BUTTON)
            assert add_to_card_button is not None, "Кнопка 'Додати в кошик' не знайдена"
            self.click_element(self.ADD_TO_CART_BUTTON)
        except:
            print('Елемент не знайдено')

    def is_product_added(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRODUCT_ADDED))
            return True
        except:
            return False
