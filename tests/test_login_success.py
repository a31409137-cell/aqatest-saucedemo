import pytest
from page_objects.login_page import LoginPage

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Проверка URL
    assert page.url == "https://www.saucedemo.com/inventory.html"

    # Проверка отображения элементов (например, заголовок "Products")
    assert page.locator("span.title").is_visible()
    assert page.locator("span.title").text_content() == "Products"