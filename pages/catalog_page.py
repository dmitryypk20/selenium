from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from config import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time


class CatalogPage(BasePage):
    SEARCH_FIELD = (By.ID, 'small-searchterms')
    PRODUCT_NOT_FOUND = (By.XPATH, "//strong[contains(text(), 'No products were found that matched your criteria.')]")
    PRODUCT_ITEM = (By.CLASS_NAME, 'product-item')
    PRODUCT_TITLE = (By.CLASS_NAME, 'product-title')
    PRODUCT_PRICE = (By.XPATH, "//span[contains(@class, 'price actual-price')]")
    DROP_DOWN_ITEM = (By.ID, 'products-orderby')
    ADVANCED_SEARCH = (By.ID, 'As')
    CATEGORY_DROP_DOWN = (By.ID, 'Cid')

    PRICE_FROM = (By.ID, 'Pf')
    PRICE_TO = (By.ID, 'Pt')
    SEARCH_BUTTON = (By.XPATH, "//input[contains(@class, 'button-1 search-button')]")

    def search_incorrect_item(self):
        self.input_text(self.SEARCH_FIELD, 'incorrect item' + Keys.ENTER)

    def search_correct_item(self):
        self.input_text(self.SEARCH_FIELD, 'computer' + Keys.ENTER)
        products = self.driver.find_elements(*self.PRODUCT_ITEM)
        print(products)
        for product in products:
            try:
                product_title = product.find_element(*self.PRODUCT_TITLE).text
                print(product_title)
                if 'computer' in product_title:
                    print('True')
            except:
                print('Помилка')

    def sorting_filter(self):
        self.input_text(self.SEARCH_FIELD, 'computer' + Keys.ENTER)
        sort_dropdown = self.find_element(self.DROP_DOWN_ITEM)
        select = Select(sort_dropdown)

        expected_options = ["Position", "Name: A to Z", "Name: Z to A", "Price: Low to High", "Price: High to Low", "Created on"]
        actual_options = [option.text for option in select.options]
        assert actual_options == expected_options, 'Список опцій не правильний'

        select.select_by_visible_text('Price: Low to High')
        time.sleep(1)

        prices = self.driver.find_elements(*self.PRODUCT_PRICE)
        prices = [int(price.text.split('.')[0]) for price in prices]
        assert prices == sorted(prices), 'Сортировка по ціні не правильна'

    def advanced_search(self):
        self.input_text(self.SEARCH_FIELD, 'computer' + Keys.ENTER)
        self.click_element(self.ADVANCED_SEARCH)

        category_dropdown = self.find_element(self.CATEGORY_DROP_DOWN)
        select = Select(category_dropdown)
        select.select_by_visible_text('All')

        # Вказуєм цінвоий діапазон
        self.input_text(self.PRICE_FROM, '500')
        self.input_text(self.PRICE_TO, '1000')
        self.click_element(self.SEARCH_BUTTON)

        # Результати пошуку
        results = self.driver.find_elements(*self.PRODUCT_ITEM)
        assert len(results) > 0, "Поиск не вернул результаты"

        # Провірка результатів цін в пошуку
        for result in results:
            price = int(result.find_element(*self.PRODUCT_PRICE).text.split(".")[0])
            assert 500 <= price <= 1000, f"Товар с некорректной ценой: {price}"

    def is_search_failed(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.PRODUCT_NOT_FOUND))
            return True
        except:
            return False
