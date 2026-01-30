# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания драйвера на каждый тест."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def page(driver):
    """Фикстура для создания LoginPage из драйвера."""
    return LoginPage(driver)