from selenium.webdriver.wpewebkit.webdriver import WebDriver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmailFrinendPage(BasePage):
    FRIEND_EMAIL = (By.ID, 'FriendEmail')
    YOUR_EMAIL = (By.ID, 'YourEmailAddress')
    PERSONAL_MESSAGE = (By.ID, 'PersonalMessage')
    SEND_EMAIL_BUTTON = (By.XPATH, "//input[contains(@class, 'button-1 send-email-a-friend-button')]")
    MESSAGE_SENT = (By.XPATH, "//div[contains(text(), 'Your message has been sent.')]")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_fields(self, friend_email, personal_message):
        your_email = 'somemeaildsds@dsadas.css'
        self.input_text(self.FRIEND_EMAIL, friend_email)
        self.input_text(self.YOUR_EMAIL, your_email)
        self.input_text(self.PERSONAL_MESSAGE, personal_message)
        self.click_element(self.SEND_EMAIL_BUTTON)

    def is_message_sent(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.MESSAGE_SENT))
            return True
        except:
            return False
