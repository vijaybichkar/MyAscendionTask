import pytest

from pages.login_page import LoginPage

@pytest.mark.order(1)
@pytest.mark.parametrize("username,password,expected", [
    ("standard_user", "secret_sauce", "inventory.html"),  # success
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),  # error
    ("invalid_user", "wrong_pass", "Username and password do not match"), #invalid
])
def test_login_roles(page, username, password, expected):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(username, password)

    if "html" in expected:  # it's a URL substring, expecting successful login
        assert expected in page.url
    else:  # expecting error message
        error_text = login_page.get_error_message()
        assert expected in error_text

@pytest.mark.order(0)
def test_blank_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("", "")
    assert "Epic sadface: Username is required" in login_page.get_error_message()
