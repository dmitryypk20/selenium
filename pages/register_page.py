from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL
from pages.base_page import BasePage

class RegisterPage(BasePage):
    # Елементи на сторінці реєстрації
    MALE_FIELD = (By.ID, 'gender-male')
    FEMALE_FIELD = (By.ID, 'gender-female')
    FIRST_NAME_FIELD = (By.ID, 'FirstName')
    LAST_NAME_FIELD = (By.ID, 'LastName')
    EMAIL_FIELD = (By.ID, 'Email')
    PASSWORD_FIELD = (By.ID, 'Password')
    CONFIRM_PASSWORD_FIELD = (By.ID, 'ConfirmPassword')
    REGISTER_BUTTON = (By.ID, 'register-button')
    LOGOUT_BUTTON = (By.CLASS_NAME, 'ico-logout')

    def __init__(self, driver):
        super().__init__(driver)

    # Метод відкриття сторінки реєстрації
    def open_page(self):
        self.driver.get(f'{BASE_URL}/register')

    def select_gender(self, gender):
        gender = gender.lower()
        if gender == 'male':
            self.click_element(self.MALE_FIELD)
        elif gender == 'female':
            self.click_element(self.FEMALE_FIELD)
        else:
            raise ValueError('Invalid gender option. Use "male" or "female"')

    def register(self, first_name, last_name, email, password, gender):
        # Заповненя полів реєстрації
        self.select_gender(gender)
        self.input_text(self.FIRST_NAME_FIELD, first_name)
        self.input_text(self.LAST_NAME_FIELD, last_name)
        self.input_text(self.EMAIL_FIELD, email)
        self.input_text(self.PASSWORD_FIELD, password)
        self.input_text(self.CONFIRM_PASSWORD_FIELD, password)
        self.click_element(self.REGISTER_BUTTON)


    def logout_user(self):
        self.click_element(self.LOGOUT_BUTTON)


    def is_registration_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGOUT_BUTTON))
            return True
        except:
            return False
