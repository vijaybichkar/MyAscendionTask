import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.order(4)
def test_sort_by_price_low_to_high(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    home_page = HomePage(page)
    home_page.sort_items_by_price_low_to_high()
    prices = home_page.get_all_item_prices()
    assert prices == sorted(prices), f"Prices not sorted from low to high! Found: {prices}"
    try:
        home_page.logout()
    except Exception as e:
        print(f"[WARN] Logout failed: {e}")

@pytest.mark.order(5)
def test_sort_by_price_high_to_low(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    home_page = HomePage(page)
    home_page.sort_items_by_price_high_to_low()
    prices = home_page.get_all_item_prices()
    expected = sorted(prices, reverse=True)
    assert prices == expected, f"Prices not sorted from high to low! Found: {prices}"
    try:
        home_page.logout()
    except Exception as e:
        print(f"[WARN] Logout failed: {e}")

@pytest.mark.order(6)
def test_sort_by_price_high_to_low(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    home_page = HomePage(page)
    home_page.sort_items_by_price_high_to_low()
    prices = home_page.get_all_item_prices()
    expected = sorted(prices, reverse=True)
    assert prices == expected, f"Prices not sorted from high to low! Found: {prices}"
    try:
        home_page.logout()
    except Exception as e:
        print(f"[WARN] Logout failed: {e}")

@pytest.mark.order(7)
def test_sort_by_A_to_Z(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    home_page = HomePage(page)
    home_page.sort_items_AtoZ()
    names = home_page.get_item_names()
    expected = sorted(names)
    assert names == expected, f"Names not sorted from A to Z! Found: {names}"
    try:
        home_page.logout()
    except Exception as e:
        print(f"[WARN] Logout failed: {e}")

@pytest.mark.order(8)
def test_sort_by_Z_to_A(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    home_page = HomePage(page)
    home_page.sort_items_ZtoA()
    names = home_page.get_item_names()
    expected = sorted(names, reverse=True)
    assert names == expected, f"Names not sorted from Z to A! Found: {names}"
    try:
        home_page.logout()
    except Exception as e:
        print(f"[WARN] Logout failed: {e}")