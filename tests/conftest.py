import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from faker import Faker
from pages.register_page import RegisterPage

fake = Faker()

@pytest.fixture(scope='session')
def registered_user(driver):
    """Фікстура реєструє користувача та повертає його дані"""

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = fake.password()
    gender = 'male'

    # Реєстрація користувача
    register_page = RegisterPage(driver)
    register_page.open_page()
    register_page.register(first_name, last_name, email, password, gender)

    # Перевіряємо, що реєстрація успішна
    assert register_page.is_registration_successful(), 'Реєстрація не вдалась'


    # Повертаємо дані користувача
    return {'email': email, 'password': password}

@pytest.fixture(scope='session')
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()
