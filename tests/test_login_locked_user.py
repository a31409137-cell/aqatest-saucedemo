import pytest
from page_objects.login_page import LoginPage

def test_login_locked_out_user(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")

    # Проверка URL
    assert page.url == "https://www.saucedemo.com/"

    # Проверка отображения сообщения об ошибке
    error_text = login_page.get_error_text()
    assert "locked out" in error_text.lower()