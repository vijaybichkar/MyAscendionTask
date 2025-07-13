import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.order(4)

def test_sort_by_price_low_to_high(page):
    """
    Test that items on the home page are sorted by price from low to high.

    Steps:
    1. Log in with standard user credentials.
    2. Sort items by price (low to high).
    3. Retrieve all item prices.
    4. Assert that the prices are sorted in ascending order.
    5. Attempt to log out, printing a warning if logout fails.

    Args:
        page: The Playwright page object used for browser automation.

    Raises:
        AssertionError: If the prices are not sorted from low to high.
    """
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    home_page = HomePage(page)
    home_page.sort_items_by_price_low_to_high()
    prices = home_page.get_all_item_prices()
    assert prices == sorted(prices), f"Prices not sorted from low to high! Found: {prices}"
    safe_logout(home_page)


@pytest.mark.order(5)
def test_sort_by_price_high_to_low(page):
    """
    Tests that items on the home page are sorted by price from high to low.

    Steps:
    1. Loads the login page and logs in with standard credentials.
    2. Navigates to the home page and sorts items by price (high to low).
    3. Retrieves all item prices and verifies they are sorted in descending order.
    4. Attempts to log out, printing a warning if logout fails.

    Args:
        page: The Playwright page object used for browser automation.

    Asserts:
        Prices are sorted from high to low after sorting action.
    """
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    home_page = HomePage(page)
    home_page.sort_items_by_price_high_to_low()
    prices = home_page.get_all_item_prices()
    expected = sorted(prices, reverse=True)
    assert prices == expected, f"Prices not sorted from high to low! Found: {prices}"
    safe_logout(home_page)


@pytest.mark.order(6)
def test_sort_by_A_to_Z(page):
    """
    Tests that the items on the home page are sorted alphabetically from A to Z after applying the sort.
    Logs in as a standard user, performs the sort, and asserts the order of item names.
    Attempts to log out at the end, printing a warning if logout fails.
    """
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    home_page = HomePage(page)
    home_page.sort_items_AtoZ()
    names = home_page.get_item_names()
    expected = sorted(names)
    assert names == expected, f"Names not sorted from A to Z! Found: {names}"
    safe_logout(home_page)


@pytest.mark.order(7)
def test_sort_by_Z_to_A(page):
    """
    Tests that the items on the home page are sorted from Z to A after applying the sort.

    Steps:
    1. Loads the login page and logs in with standard credentials.
    2. Navigates to the home page and applies the "Z to A" sorting.
    3. Retrieves the list of item names and checks if they are sorted in descending order.
    4. Asserts that the actual order matches the expected Z to A order.
    5. Attempts to log out, printing a warning if logout fails.

    Args:
        page: The Playwright page object used for browser interaction.

    Raises:
        AssertionError: If the items are not sorted from Z to A.
    """
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    home_page = HomePage(page)
    home_page.sort_items_ZtoA()
    names = home_page.get_item_names()
    expected = sorted(names, reverse=True)
    assert names == expected, f"Names not sorted from Z to A! Found: {names}"
    safe_logout(home_page)

def safe_logout(home_page):
    try:
        home_page.logout()
    except Exception as e:
        print(f"[WARN] Logout failed: {e}")