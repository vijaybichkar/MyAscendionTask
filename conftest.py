import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser_context(playwright_instance, request):
    browser = playwright_instance.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()
    browser.close()

@pytest.fixture(scope="function")
def logged_in_user(browser_context):
    login_page = LoginPage(browser_context)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    home_page = HomePage(browser_context)

    yield home_page  # test will use this

    # Cleanup: logout
    home_page.logout()
