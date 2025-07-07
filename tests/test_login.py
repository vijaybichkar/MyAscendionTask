
from pages.login_page import LoginPage
from pages.home_page import HomePage

def login_as_standard_user(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    return HomePage(page)

def test_successful_login(browser_context):
    login_page = LoginPage(browser_context)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert browser_context.url == "https://www.saucedemo.com/inventory.html"

def test_invalid_login(browser_context):
    login_page = LoginPage(browser_context)
    login_page.load()
    login_page.login("invalid_user", "wrong_password")
    assert "Username and password do not match" in login_page.get_error_message()

def test_add_to_cart(browser_context):
    home_page = login_as_standard_user(browser_context)
    home_page.add_item_to_cart()
    assert home_page.get_cart_count() == 1

    home_page.go_to_cart()
    assert "cart" in browser_context.url

def test_logout(browser_context):
    home_page = login_as_standard_user(browser_context)
    home_page.logout()
    assert browser_context.url == "https://www.saucedemo.com/"