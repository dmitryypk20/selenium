from pages.home_page import HomePage
import allure

@allure.feature('Перевірка каталогів')
@allure.story('Успішний перехід між каталогами')
@allure.title('Тест працездатності каталоів')
def test_category(driver):
    home_page = HomePage(driver)
    home_page.go_to_category()
    home_page.add_product_to_cart()
    assert home_page.is_product_added(), 'Товар не додано'
