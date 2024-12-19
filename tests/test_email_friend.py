from pages.email_friend_page import EmailFrinendPage
from pages.product_page import ProductPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
import allure

import pytest
from faker import Faker


@allure.feature('Залишення емейлу')
@allure.story('Відправлення емелйу')
@allure.title('Тест відправлення емейлу')
def test_email_friend(driver, generate_fake_data):
    friend_email, personal_messge = generate_fake_data
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    login_page = LoginPage(driver)
    email_friend_page = EmailFrinendPage(driver)
    login_page.login_to_account()
    home_page.go_to_product()
    product_page.email_friend()
    email_friend_page.fill_fields(friend_email, personal_messge)
    assert email_friend_page.is_message_sent(), 'Повідомлення не було надіслано'


fake = Faker()


@pytest.fixture
def generate_fake_data():
    friend_email = fake.email()
    personal_message = fake.text()

    return friend_email, personal_message
