FROM python:3.10-slim

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Установка Playwright и его браузеров
RUN playwright install --with-deps chromium

# Копирование кода тестов
COPY tests/ ./tests/

# Запуск тестов
CMD ["pytest", "tests/", "--headless"]