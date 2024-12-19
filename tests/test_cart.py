import pytest
import allure
from faker import Faker
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.login_page import LoginPage

import time


@allure.feature('Корзина покупок')
@allure.story('Додавання товару в кошик')
@allure.title('Тест додавання товару в кошик')
def test_add_product_to_cart(driver):
    home_page = HomePage(driver)
    cart_page = CartPage(driver)

    home_page.open_page()
    home_page.add_product_to_cart()
    if home_page.is_product_added():
        allure.attach(driver.get_screenshot_as_png(), name="Product added to cart", attachment_type=allure.attachment_type.PNG)
        print('Товар добавлено у кошик')
    else:
        allure.attach(driver.get_screenshot_as_png(), name="Product not added to cart", attachment_type=allure.attachment_type.PNG)
        print('Товар не було добавлено у кошик')
    home_page.go_to_cart()


@allure.feature('Корзина покупок')
@allure.story('Видалення товару з кошика')
@allure.title('Тест видалення товару з кошика')
def test_remove_product_from_cart(driver):
    home_page = HomePage(driver)
    cart_page = CartPage(driver)

    # Добавити товар в коризну
    home_page.open_page()
    home_page.add_product_to_cart()
    home_page.go_to_cart()

    cart_page.remove_from_cart()
    if cart_page.is_cart_empty():
        allure.attach(driver.get_screenshot_as_png(), name="Product removed from cart", attachment_type=allure.attachment_type.PNG)
        print('Товар видалено із кошика')
    else:
        allure.attach(driver.get_screenshot_as_png(), name="Product not removed from cart", attachment_type=allure.attachment_type.PNG)
        print('Товар не видалено із кошика')



@allure.feature('Корзина покупок')
@allure.story('Перевірка кількості товарів у кошику')
@allure.title('Тест перевірки кількості товарів у кошику')
def test_product_quantity_in_cart(driver):
    home_page = HomePage(driver)
    cart_page = CartPage(driver)

    # Відкрити товар і добавити декілька продуктів
    home_page.open_page()
    home_page.add_product_to_cart()  # Добавити продукт
    time.sleep(1)
    home_page.add_product_to_cart()  # Добавити другий продукт
    time.sleep(1)
    home_page.go_to_cart()

    products_quantity = cart_page.amount_of_products().replace('(', '').replace(')', '')
    assert products_quantity == '2', f'Очікувана кількість товарів у кошику - 2, але знайдено {products_quantity}'
    allure.attach(driver.get_screenshot_as_png(), name="Cart products quantity", attachment_type=allure.attachment_type.PNG)
    print(f'У кошику {products_quantity} товарів')



@allure.feature('Замовлення')
@allure.story('Оформлення замовлення')
@allure.title('Тест оформлення замовлення')
def test_order_checkout(driver, fake_user_data):
    home_page = HomePage(driver)
    cart_page = CartPage(driver)
    login_page = LoginPage(driver)

    city, address1, address2, zip_code, phone_number, fax_number = fake_user_data

    login_page.go_to_login_page()
    login_page.login_to_account()

    home_page.open_page()
    home_page.add_product_to_cart()
    time.sleep(1)
    home_page.go_to_cart()

    cart_page.order_checkout()
    time.sleep(1)
    if not login_page.is_login_succesful():
        cart_page.fill_billing_address(city, address1, address2, zip_code, phone_number, fax_number)
        allure.attach(driver.get_screenshot_as_png(), name="Checkout step - Billing Address", attachment_type=allure.attachment_type.PNG)
    time.sleep(5)
    cart_page.complete_checkout_process()
    allure.attach(driver.get_screenshot_as_png(), name="Checkout completed", attachment_type=allure.attachment_type.PNG)


fake = Faker()

@pytest.fixture
def fake_user_data():
    city = fake.city()
    address1 = fake.address().splitlines()[0]
    address2 = fake.secondary_address()
    zip_code = fake.zipcode()
    phone_number = fake.phone_number()
    fax_number = fake.phone_number()

    return city, address1, address2, zip_code, phone_number, fax_number
