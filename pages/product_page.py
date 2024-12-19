from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from config import BASE_URL

class ProductPage(BasePage):
    ADD_REVIEW_LINK = (By.XPATH, "//a[contains(text(), 'Add your review')]")
    COMPARE_LIST_BUTTON = (By.XPATH, "//input[contains(@class, 'button-2 add-to-compare-list-button')]")
    EMAIL_FRIEND = (By.XPATH, "//input[contains(@class, 'button-2 email-a-friend-button')]")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_add_review(self):
        self.click_element(self.ADD_REVIEW_LINK)


    def add_to_compare_list(self):
        self.click_element(self.COMPARE_LIST_BUTTON)

    def email_friend(self):
        self.click_element(self.EMAIL_FRIEND)


    def go_to_compare_list(self):
        self.driver.get(f'{BASE_URL}/compareproducts')
