import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

def login_as_standard_user(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    return HomePage(page)

# @pytest.mark.dependency(name="login")
@pytest.mark.order(1)
def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

@pytest.mark.order(0)
def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("invalid_user", "wrong_password")
    assert "Username and password do not match" in login_page.get_error_message()

@pytest.mark.smoke
def test_blank_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("", "")
    assert "Epic sadface: Username is required" in login_page.get_error_message()

def test_logout(page):
    home_page = login_as_standard_user(page)
    home_page.logout()
    assert page.url == "https://www.saucedemo.com/"