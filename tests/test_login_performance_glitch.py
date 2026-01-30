import pytest
from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage

def test_login_performance_glitch_user(page):
    page.open()
    page.login("performance_glitch_user", "secret_sauce")
    
    # Проверяем, что попали на inventory.html (даже при "glitch")
    assert "/inventory.html" in page.driver.current_url

    title_elem = page.driver.find_element(By.CSS_SELECTOR, "span.title")
    assert title_elem.text == "Products"