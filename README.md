# Автотесты для SauceDemo (Python + Selenium + pytest)

Репозиторий содержит автоматизированные UI-тесты для сайта [https://www.saucedemo.com](https://www.saucedemo.com) на основе Page Object Model.

Все тесты проходят локально (проверено на Python 3.14, Selenium 4.40).

---

## Требования

- Python 3.8+
- Chrome (для запуска тестов в браузере)
- Internet (для доступа к saucedemo.com)

---

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/a31409137-cell/aqatest-saucedemo.git
   cd aqatest-saucedemo
   ```
2. Установите зависимости:
   ```bash
   python -m pip install -r requirements.txt
   # или, если requirements.txt пуст:
   python -m pip install pytest selenium webdriver-manager
   ```
3. Запустите все тесты:
   ```bash
   python -m pytest tests/ -v
   ```