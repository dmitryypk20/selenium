import pytest
import allure
from pages.catalog_page import CatalogPage
from pages.home_page import HomePage

import time


@allure.feature('Пошук товарів')
@allure.story('Некоректний пошук')
@allure.title('Тест некоректного введення у пошук')
def test_incorrect_input(driver):
    home_page = HomePage(driver)
    catalog_page = CatalogPage(driver)
    home_page.open_page()
    catalog_page.search_incorrect_item()
    assert catalog_page.is_search_failed(), 'Пошук мав би не вдатись'
    allure.attach(driver.get_screenshot_as_png(), name="Incorrect search attempt", attachment_type=allure.attachment_type.PNG)
    print('Пошук успішний')


@allure.feature('Пошук товарів')
@allure.story('Коректний пошук')
@allure.title('Тест коректного введення у пошук')
def test_correct_input(driver):
    home_page = HomePage(driver)
    catalog_page = CatalogPage(driver)
    home_page.open_page()
    catalog_page.search_correct_item()
    allure.attach(driver.get_screenshot_as_png(), name="Correct search result", attachment_type=allure.attachment_type.PNG)


@allure.feature('Фільтрація та сортування')
@allure.story('Тестування фільтрації та сортування')
@allure.title('Тест фільтрації та сортування товарів')
def test_sorting_filter(driver):
    home_page = HomePage(driver)
    catalog_page = CatalogPage(driver)
    home_page.open_page()
    catalog_page.sorting_filter()
    allure.attach(driver.get_screenshot_as_png(), name="Sorting and filter applied", attachment_type=allure.attachment_type.PNG)


@allure.feature('Пошук товарів')
@allure.story('Розширений пошук')
@allure.title('Тест розширеного пошуку')
def test_advanced_search(driver):
    home_page = HomePage(driver)
    catalog_page = CatalogPage(driver)
    home_page.open_page()
    catalog_page.advanced_search()
    allure.attach(driver.get_screenshot_as_png(), name="Advanced search result", attachment_type=allure.attachment_type.PNG)
