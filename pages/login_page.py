from selenium.webdriver.wpewebkit.webdriver import WebDriver
from config import BASE_URL
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    # Елементи на сторінці авторизації
    EMAIL_FIELD = (By.ID, 'Email')
    PASSWORD_FIELD = (By.ID, 'Password')
    REMEMBER_ME_BUTTON = (By.ID, 'RememberMe')
    LOGIN_BUTTON = (By.XPATH, "//input[contains(@class, 'login-button')]")
    USER_NOT_FOUND_ERROR = (By.XPATH, "//li[contains(text(), 'No customer account found')]")
    INVALID_EMAIL_ERROR = (By.XPATH, "//span[contains(text(), 'Please enter a valid email address.')]")
    LOGGED_USER = (By.CLASS_NAME, 'ico-logout')

    def __init__(self, driver):
        super().__init__(driver)


    def go_to_login_page(self):
        self.driver.get(f'{BASE_URL}/login')


    def login(self, email, password):
        self.input_text(self.EMAIL_FIELD, email)
        self.input_text(self.PASSWORD_FIELD, password)
        self.click_element(self.REMEMBER_ME_BUTTON)
        self.click_element(self.LOGIN_BUTTON)

    def login_to_account(self):
        email = 'somemeaildsds@dsadas.css'
        password = 'password123'
        self.go_to_login_page()
        self.input_text(self.EMAIL_FIELD, email)
        self.input_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)


    def is_login_succesful(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((self.LOGGED_USER)))
            return True
        except:
            return False

    def is_login_failed(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.USER_NOT_FOUND_ERROR))
            return True
        except:
            return False


    def is_email_invalid(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.INVALID_EMAIL_ERROR))
            return True
        except:
            return False
