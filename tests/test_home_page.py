import pytest 

@pytest.mark.order(2)
def test_home_page(logged_in_user):
    page = logged_in_user.page

    assert "inventory.html" in page.url

def test_add_and_remove_button_functionality(logged_in_user):
    page = logged_in_user.page

    # Add item to cart
    logged_in_user.add_item_to_cart()

    # Check that cart badge shows 1
    assert logged_in_user.get_cart_count() == 1, "Cart count after adding should be 1"
    page.locator("button[id^='remove-sauce']").first.click()

def test_remove_button_functionality(logged_in_user):
    page = logged_in_user.page

    # Add item first
    logged_in_user.add_item_to_cart()

    # Remove it
    page.locator("button[id^='remove-sauce']").first.click()

    # Check the cart badge disappears or resets
    cart_badge = page.locator(".shopping_cart_badge")
    assert not cart_badge.is_visible(), "Cart badge should disappear after removing item"
