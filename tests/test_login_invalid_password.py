import pytest
from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage

def test_login_with_invalid_password(page):
    page.open()
    page.login("standard_user", "wrong_password")
    
    error_elem = page.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert "Username and password do not match" in error_elem.text