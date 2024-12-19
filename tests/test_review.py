import pytest
from faker import Faker
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.review_page import ReviewPage
from pages.login_page import LoginPage
import allure
import time

fake = Faker()


@pytest.fixture
def generate_fake_review():
    review_title = fake.sentence()
    review_text = fake.paragraph()

    return review_title, review_text


@allure.feature('Залишення відгуку')
@allure.story('Успішно залишений відгук')
@allure.title('Тест залишення відгуку')
def test_review(driver, generate_fake_review):
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    review_page = ReviewPage(driver)
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login_to_account()
    review_title, review_text = generate_fake_review
    home_page.go_to_product()
    product_page.go_to_add_review()
    review_page.fill_review(review_title, review_text)
    assert review_page.is_review_added(), 'Відгук не був залишений'
