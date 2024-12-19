import allure
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class CartPage(BasePage):
    # Елементи на сторінці кошика
    CART_IS_EMPTY = (By.XPATH, "//div[contains(text(), 'Your Shopping Cart is empty!')]")
    ITEM_ELEMENT = (By.XPATH, "//input[contains(@name, 'removefromcart')]")
    UPDATE_CART_BUTTON = (By.XPATH, "//input[contains(@value, 'Update shopping cart')]")
    PRODUCTS_QUANTITY = (By.XPATH, "//span[contains(@class, 'cart-qty')]")
    TERMS_OF_SERVICE_CHECKBOX = (By.ID, 'termsofservice')
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    COUNTRY_FIELD = (By.ID, 'BillingNewAddress_CountryId')
    CITY_FIELD = (By.ID, 'BillingNewAddress_City')
    ADDRESS1_FIELD = (By.ID, 'BillingNewAddress_Address1')
    ADDRESS2_FIELD = (By.ID, 'BillingNewAddress_Address2')
    ZIP_FIELD = (By.ID, 'BillingNewAddress_ZipPostalCode')
    PHONE_NUMBER_FIELD = (By.ID, 'BillingNewAddress_PhoneNumber')
    FAX_NUMBER = (By.ID, 'BillingNewAddress_FaxNumber')

    LOADING_TEXT = (By.ID, 'payment-info-please-wait')

    BILLING_METHOD_BUTTON = (By.XPATH, "//input[contains(@onclick, 'Billing.save()')]")
    SHIPPING_BUTTON = (By.XPATH, "//input[contains(@onclick, 'Shipping.save()')]")
    SHIPPING_METHOD_BUTTON = (By.XPATH, "//input[contains(@onclick, 'ShippingMethod.save()')]")
    PAYMENT_METHOD_BUTTON = (By.XPATH, "//input[contains(@onclick, 'PaymentMethod.save()')]")
    PAYMENT_INFO_BUTTON = (By.XPATH, "//input[contains(@onclick, 'PaymentInfo.save()')]")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//input[contains(@onclick, 'ConfirmOrder.save()')]")
    ADRESS_SELECTED = (By.XPATH, "//select[contains(@class, 'address-select valid')]")

    CONTINUE_BUTTON = (By.XPATH, "//input[contains(@onclick, 'Billing.save()')]")

    def __init__(self, driver):
      super().__init__(driver)


    def is_cart_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CART_IS_EMPTY))
            return True
        except:
            return False


    def remove_from_cart(self):
        self.driver.find_element(*self.ITEM_ELEMENT).click()
        self.click_element(self.UPDATE_CART_BUTTON)


    def amount_of_products(self):
        return self.get_text(self.PRODUCTS_QUANTITY)


    def order_checkout(self):
        self.click_element(self.TERMS_OF_SERVICE_CHECKBOX)
        self.click_element(self.CHECKOUT_BUTTON)


        self.execute_button_js(self.CONTINUE_BUTTON, 'Billing.save()')

    def fill_billing_address(self, city, address1, address2, zip_code, phone_number, fax_number):
        select = Select(self.find_element(self.COUNTRY_FIELD))
        select.select_by_index(2)
        self.input_text(self.CITY_FIELD, city)
        self.input_text(self.ADDRESS1_FIELD, address1)
        self.input_text(self.ADDRESS2_FIELD, address2)
        self.input_text(self.ZIP_FIELD, zip_code)
        self.input_text(self.PHONE_NUMBER_FIELD, phone_number)
        self.input_text(self.FAX_NUMBER, fax_number)
        self.click_element(self.BILLING_METHOD_BUTTON)

    def execute_button_js(self, button_locator, js_function):
        """
        Виконує JavaScript функцію для кнопки та чекає оновлення сторінки
        """
        # Чекаємо поки кнопка стане клікабельною
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        )

        # Виконуємо JavaScript
        self.driver.execute_script(f"{js_function}")

        # Чекаємо поки пропаде індикатор завантаження
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.LOADING_TEXT)
        )

    def complete_checkout_process(self):
        """Проходження всіх кроків оформлення замовлення"""
        # Крок 1: Shipping Method
        self.execute_button_js(self.SHIPPING_BUTTON, "Shipping.save()")

        self.execute_button_js(self.SHIPPING_METHOD_BUTTON, "ShippingMethod.save()")
        # Крок 2: Payment Method
        self.execute_button_js(self.PAYMENT_METHOD_BUTTON, "PaymentMethod.save()")

        # Крок 3: Payment Information
        self.execute_button_js(self.PAYMENT_INFO_BUTTON, "PaymentInfo.save()")

        # Крок 4: Confirm Order
        self.execute_button_js(self.CONFIRM_ORDER_BUTTON, "ConfirmOrder.save()")
