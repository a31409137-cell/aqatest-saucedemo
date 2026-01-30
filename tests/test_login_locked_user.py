import pytest
from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage

def test_login_locked_out_user(page):
    page.open()
    page.login("locked_out_user", "secret_sauce")
    
    error_elem = page.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert "locked out" in error_elem.text.lower()