import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.checkout_page import CheckoutPage

@pytest.mark.order(5)
def test_checkout_flow(page):
    # Login
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Add to cart and go to cart page
    home_page = HomePage(page)
    home_page.add_item_to_cart()
    home_page.go_to_cart()

    # Click checkout
    page.locator('[data-test="checkout"]').click()

    # Fill in checkout info and finish
    checkout_page = CheckoutPage(page)
    checkout_page.fill_customer_info("Vijay", "Bichkar", "12345")
    checkout_page.continue_checkout()

    assert "checkout-step-two" in page.url

    checkout_page.finish_checkout()

    assert "Thank you for your order!" in checkout_page.get_complete_header()
