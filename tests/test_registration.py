import pytest
import allure
from faker import Faker
from pages.register_page import RegisterPage

fake = Faker()

@pytest.fixture
def fake_user_data():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = fake.password()
    gender = 'male'
    return first_name, last_name, email, password, gender

# Тест для реєстрації
@allure.feature('Реєстрація користувача')
@allure.story('Успішна реєстрація')
@allure.title('Тест реєстрації користувача')
def test_registration(driver, fake_user_data):
    first_name, last_name, email, password, gender = fake_user_data
    register_page = RegisterPage(driver)
    register_page.open_page()

    # Виконуєм реєстрацію
    with allure.step('Заповнення фейкових даних у поля'):
        register_page.register(first_name, last_name, email, password, gender)

    with allure.step('Провірка чи була реєстрація та відповідно авторизація успішними'):
        assert register_page.is_registration_successful(),  'Реєстрація успішна'

    if not register_page.is_registration_successful():
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
