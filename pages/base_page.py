from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class BasePage:
    def __init__(self, driver=None):
        if driver == None:
            service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service)
        else:
            self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, timeout=10):
        self.find_element(locator, timeout).click()

    def input_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        return self.find_element(locator, timeout).text
