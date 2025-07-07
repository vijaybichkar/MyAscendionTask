import logging
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.home_page import HomePage

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def page(playwright_instance, request):
    browser = playwright_instance.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

@pytest.fixture(scope="function")
def logged_in_user(page):

    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    home_page = HomePage(page)
    yield home_page
    logger.info("Attempting login")
    try:
        if "inventory.html" in page.url:
            home_page.logout()
    except Exception as e:
        print(f"[WARN] Logout failed during teardown: {e}")
