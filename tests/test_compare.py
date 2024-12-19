import pytest
import allure
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.compare_page import ComparePage

import time


@allure.feature('Перевірка вікна порівняння')
@allure.story('Вікно пораівння')
@allure.title('Тест порівняння')
def test_compare(driver):
    product_page = ProductPage(driver)
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    compare_page = ComparePage(driver)
    home_page.open_page()
    home_page.go_to_product()
    product_page.add_to_compare_list()
    assert not compare_page.is_compare_list_empty(), 'Таблиця порожня'
    compare_page.remove_from_compare_list()
    time.sleep(2)
    assert compare_page.is_compare_list_empty(), 'Таблиця не порожня'
