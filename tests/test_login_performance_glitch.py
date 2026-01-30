import pytest
from page_objects.login_page import LoginPage

def test_login_performance_glitch_user(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("performance_glitch_user", "secret_sauce")

    # Проверка URL
    assert page.url == "https://www.saucedemo.com/inventory.html"

    # Проверка отображения элементов (страница должна открыться несмотря на задержки)
    assert page.locator("span.title").is_visible()
    assert page.locator("span.title").text_content() == "Products"