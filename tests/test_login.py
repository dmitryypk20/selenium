import pytest
import allure
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


@allure.feature('Авторизація')
@allure.story('Логін з невідомим користувачем')
@allure.title('Тест логіну з невідомим користувачем')
def test_login_no_user(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login('Userdoes@not.exist', 'password')
    allure.attach(driver.get_screenshot_as_png(), name="Login failed for non-existing user", attachment_type=allure.attachment_type.PNG)
    assert login_page.is_login_failed(), 'Очікувалось повідомлення про помилку але його немає'


@allure.feature('Авторизація')
@allure.story('Невірний формат email')
@allure.title('Тест логіну з невірним форматом email')
def test_invalid_email_format(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login('invalidemail.gmail.com', 'password')
    allure.attach(driver.get_screenshot_as_png(), name="Invalid email format error", attachment_type=allure.attachment_type.PNG)
    assert login_page.is_email_invalid(), 'Помилка про неправильний формат емейлу відстуня'



@allure.feature('Авторизація')
@allure.story('Логін з валідними даними')
@allure.title('Тест логіну з валідними даними')
def test_login_with_valid_data(driver, registered_user):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()

    # Отримаємо дані зареєстрованого користувача
    email = registered_user['email']
    password = registered_user['password']

    # Виходимо з акканту, тому що після реєстрації система автоматично авторизується
    register_page = RegisterPage(driver)
    register_page.logout_user()

    # Виконуємо логін
    login_page.go_to_login_page()
    login_page.login(email, password)
    allure.attach(driver.get_screenshot_as_png(), name="Successful login", attachment_type=allure.attachment_type.PNG)

    # Перевірка чи авторизація успішна
    assert login_page.is_login_succesful(), 'Авторизація на вдалась з валідними даними'
