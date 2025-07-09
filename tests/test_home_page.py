import pytest

@pytest.mark.order(3)
def test_add_and_remove_button_functionality(logged_in_user):
    page = logged_in_user.page

    try:
        logged_in_user.add_item_to_cart()
        assert logged_in_user.get_cart_count() == 1, "Cart count after adding should be 1"
        page.locator("button[id^='remove-sauce']").first.click()
        cart_badge = page.locator(".shopping_cart_badge")
        assert not cart_badge.is_visible(), "Cart badge should disappear after removing item"

    except Exception as e:
        pytest.fail(f"Test failed in test_add_and_remove_button_functionality: {e}")


@pytest.mark.order(4)
def test_remove_button_functionality(logged_in_user):
    page = logged_in_user.page

    try:
        logged_in_user.add_item_to_cart()
        page.locator("button[id^='remove-sauce']").first.click()
        cart_badge = page.locator(".shopping_cart_badge")
        assert not cart_badge.is_visible(), "Cart badge should disappear after removing item"

    except Exception as e:
        pytest.fail(f"Test failed in test_remove_button_functionality: {e}")

@pytest.mark.order(2)
def test_incorrect_product_description(logged_in_user):
    try:
        page = logged_in_user.page
        first_product_desc = logged_in_user.get_first_product_description()
        expected_desc = "Carry all the things with the sleek, streamlined Sly Pack that melds uncompromising style"
        assert first_product_desc == expected_desc, f"Expected description: '{expected_desc}', but got: '{first_product_desc}'"
    except Exception as e:
        pytest.fail(f"Test failed due to an unexpected error: {e}")

def test_incorrect_last_product_label(logged_in_user):
    try:
        page = logged_in_user.page
        last_product_label = logged_in_user.get_last_product_label()
        expected_label = "T-Shirt (Red)"
        assert last_product_label == expected_label, f"Expected label: '{expected_label}', but got: '{last_product_label}'"
    except Exception as e:
        pytest.fail(f"Test failed due to an unexpected error: {e}")