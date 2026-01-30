import pytest
from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage

def test_successful_login(page):
    page.open()
    page.login("standard_user", "secret_sauce")
    
    # Проверка: мы на странице инвентаря
    assert "/inventory.html" in page.driver.current_url

    # Дополнительно: проверка видимого заголовка
    title_elem = page.driver.find_element(By.CSS_SELECTOR, "span.title")
    assert title_elem.text == "Products"