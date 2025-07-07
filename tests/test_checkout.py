from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.checkout_page import CheckoutPage


def test_checkout_flow(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    home_page = HomePage(page)
    try:
        home_page.add_item_to_cart()
        home_page.go_to_cart()

        page.locator('[data-test="checkout"]').click()

        checkout_page = CheckoutPage(page)
        checkout_page.fill_customer_info("Vijay", "Bichkar", "12345")
        checkout_page.continue_checkout()

        assert "checkout-step-two" in page.url

        checkout_page.finish_checkout()

        assert "Thank you for your order!" in checkout_page.get_complete_header()

    finally:
        # This runs no matter what - even if test fails
        try:
            home_page.logout()
        except Exception as e:
            print(f"Logout failed during teardown: {e}")
