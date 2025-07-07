import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.order(1)
@pytest.mark.parametrize("username,password,expected", [
    ("standard_user", "secret_sauce", "inventory.html"),  # success
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),  # error
    ("invalid_user", "wrong_pass", "Username and password do not match"),  # invalid credentials
])
def test_login_roles(page, username, password, expected):
    login_page = LoginPage(page)
    login_page.load()

    try:
        login_page.login(username, password)

        if "html" in expected:
            assert expected in page.url
        else:
            error_text = login_page.get_error_message()
            assert expected in error_text

    except Exception as e:
        pytest.fail(f"Test failed for user {username}: {e}")

    finally:
        # Attempt logout if login was successful
        try:
            if "inventory.html" in page.url:
                home_page = HomePage(page)
                home_page.logout()
        except Exception as e:
            print(f"[WARN] Logout failed for user {username}: {e}")


@pytest.mark.order(0)
def test_blank_login(page):
    login_page = LoginPage(page)
    login_page.load()

    try:
        login_page.login("", "")
        assert "Epic sadface: Username is required" in login_page.get_error_message()

    except Exception as e:
        pytest.fail(f"Blank login test failed: {e}")
