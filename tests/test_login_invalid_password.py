import pytest
from page_objects.login_page import LoginPage

def test_login_with_invalid_password(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "wrong_password")

    # Проверка URL (должна остаться на той же странице)
    assert page.url == "https://www.saucedemo.com/"

    # Проверка отображения сообщения об ошибке
    error_text = login_page.get_error_text()
    assert "Username and password do not match" in error_text