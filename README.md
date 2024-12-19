# Фреймворк для автоматизованого тестування інтернет-магазину

Цей фреймворк призначений для автоматизації тестування функціональності інтернет-магазину, використовуючи **Selenium**, **webdriver-manager**, **Pytest** та **Allure** для зручності створення та виконання тестів, а також для генерації звітів.

## Основні можливості

-   Тестування критичних функцій інтернет-магазину.
-   Генерація звітів про результати тестів.

## Вимоги

-   Python 3.8+
-   Google Chrome (остання версія)

## Встановлення

### 1. Клонування репозиторію:

```bash
git clone https://github.com/dmitryypk20/web-automation-with-selenium.git
cd web-automation-with-selenium
```

### 2. Створення та активація віртуального середовища:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Встановлення залежностей:

```bash
pip install -r requirements.txt
```

## Структура проєкту

```plaintext
web-automation-with-selenium/
├── pages/                 # Модулі Page Object для різних сторінок
│   ├── base_page.py       # Базовий клас для всіх сторінок
│   ├── home_page.py       # Модуль для головної сторінки
│   └── cart_page.py       # Модуль для сторінки кошика
│   └── catalog_page.py    # Модуль для сторінки каталоу
│   └── login_page.py      # Модуль для сторінки входу
│   └── register_page.py   # Модуль для сторінки реєстрації
├── tests/                 # Тестові сценарії
│   ├── test_login.py      # Тести для функціоналу логіну
│   └── test_catalog.py    # Тести для функціоналу каталогу
│   └── test_cart.py       # Тести для функціоналу кошика
│   └── conftest.py        # Тести для процесу оформлення замовлення
│   └── test_registration.py  # Тести для функціоналу реєстрації
├── config.py              # Конфігураційні налаштування
├── requirements.txt       # Список залежностей
└── README.md              # Опис проєкту
```

## Запуск тестів

### 1. Запуск тестів за допомогою Pytest:

```bash
pytest
```

### 2. Генерація звітів Allure:

1. Встановіть **Allure Commandline**, дотримуючись [офіційної документації](https://allurereport.org/docs/install/).
2. Запустіть тести з генерацією даних для Allure:
    ```bash
    pytest --alluredir=reports/
    ```
3. Згенеруйте та відкрийте звіт:
    ```bash
    allure serve reports/
    ```

## Додавання нових тестів

### 1. Створення нового модуля в директорії `tests/`:

```python
# tests/test_example.py
import pytest
from pages.home_page import HomePage

def test_example(driver):
    home = HomePage(driver)
    home.load()
    assert home.is_loaded()
```

### 2. Використання підходу Page Object Model (POM):

Створіть новий клас у директорії `pages/`, який представляє сторінку, з якою ви взаємодієте.

```python
# pages/example_page.py
from pages.base_page import BasePage

class ExamplePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.example_element = 'css_selector'

    def interact_with_element(self):
        self.find_element(self.example_element).click()
```

## Пояснення до основних файлів та директорій

### `pages/`

Ця директорія містить модулі, що реалізують Page Object для різних сторінок інтернет-магазину. Кожен модуль відповідає за одну сторінку та містить методи для взаємодії з елементами цієї сторінки.

### `tests/`

Тестові сценарії для перевірки функціональності веб-сайту. Тести повинні бути описані відповідно до кожної критичної функції сайту, наприклад, авторизація чи оформлення замовлення.

### `config.py`

Файл конфігурації для зберігання налаштувань, таких як параметри браузера, URL базового сайту тощо.
