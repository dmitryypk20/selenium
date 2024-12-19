from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ComparePage(BasePage):
    # Елементи на сторінці порівнювання
    REMOVE_FROM_COMPARE_LIST_BUTTON = (By.XPATH, "//input[contains(@class, 'button-2 remove-button')]")
    NO_PRODUCT_IN_COMPARE_LIST = (By.XPATH, "//div[contains(text(), 'You have no items to compare.')]")

    def __init__(self, driver):
        super().__init__(driver)

    def remove_from_compare_list(self):
            self.click_element(self.REMOVE_FROM_COMPARE_LIST_BUTTON)

    def is_compare_list_empty(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.NO_PRODUCT_IN_COMPARE_LIST))
            return True
        except:
            return False
