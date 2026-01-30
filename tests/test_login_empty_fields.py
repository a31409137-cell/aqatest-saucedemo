import pytest
from page_objects.login_page import LoginPage

def test_login_with_empty_fields(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("", "")

    # Проверка URL
    assert page.url == "https://www.saucedemo.com/"

    # Проверка отображения сообщения об ошибке
    error_text = login_page.get_error_text()
    assert "Username is required" in error_text