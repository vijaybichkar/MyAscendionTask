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
    assert prices == sorted(prices), f"Prices not sorted! Found: {prices}"
    try:
        home_page.logout()
    except Exception as e:
        print(f"[WARN] Logout failed: {e}")
