import pytest 

@pytest.mark.order(2)
def test_add_and_remove_button_functionality(logged_in_user):
    page = logged_in_user.page
    logged_in_user.add_item_to_cart()
    assert logged_in_user.get_cart_count() == 1, "Cart count after adding should be 1"
    page.locator("button[id^='remove-sauce']").first.click()


@pytest.mark.order(3)
def test_remove_button_functionality(logged_in_user):
    page = logged_in_user.page
    logged_in_user.add_item_to_cart()
    page.locator("button[id^='remove-sauce']").first.click()
    cart_badge = page.locator(".shopping_cart_badge")
    assert not cart_badge.is_visible(), "Cart badge should disappear after removing item"

