from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

class ReviewPage(BasePage):
    # Елементи на сторінці відгуків
    REVIEW_TITLE = (By.ID, 'AddProductReview_Title')
    REVIEW_TEXT = (By.ID, 'AddProductReview_ReviewText')
    RATING_RADIO = (By.ID, 'addproductrating_4')
    SUBMIT_REVIEW_BUTTON = (By.XPATH, "//input[contains(@class, 'button-1 write-product-review-button')]")
    REVIEW_ADDED = (By.XPATH, "//div[contains(text(), 'Product review is successfully added.')]")


    def __init__(self, driver):
        super().__init__(driver)


    def fill_review(self, review_title, review_text):
        self.input_text(self.REVIEW_TITLE, review_title)
        self.input_text(self.REVIEW_TEXT, review_text)
        self.click_element(self.RATING_RADIO)
        time.sleep(1)
        self.click_element(self.SUBMIT_REVIEW_BUTTON)

    def is_review_added(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.REVIEW_ADDED))
            return True
        except:
            return False

    # def find_review(self):
