import pytest
from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage

def test_login_with_empty_fields(page):
    page.open()
    page.login("", "")
    
    error_elem = page.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert "Username is required" in error_elem.text