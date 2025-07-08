class HomePage:
    def __init__(self, page):
        self.page = page
        self.burger_menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")
        self.cart_button = page.locator(".shopping_cart_link")
        self.add_to_cart_button = page.locator("button[data-test='add-to-cart-sauce-labs-backpack']")
        self.remove_button = page.locator("#remove-sauce-labs-backpack")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def logout(self):
        self.burger_menu_button.click()
        self.page.wait_for_timeout(500)  # Allow menu to expand
        self.logout_link.click()

    def add_item_to_cart(self):
        self.add_to_cart_button.click()

    def remove_item_from_cart(self):
        self.remove_button.click()

    def go_to_cart(self):
        self.cart_button.click()

    def get_cart_count(self):
        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content())
        return 0
    
    def add_item_to_cart(self):
        self.page.locator("button[id^='add-to-cart']").first.click()

    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()

    def sort_items_by_price_low_to_high(self):
        self.page.locator('.product_sort_container').click()
        self.page.locator('.product_sort_container').select_option("lohi")


    def sort_items_by_price_high_to_low(self):
        self.page.locator('.product_sort_container').click()
        self.page.locator('.product_sort_container').select_option("hilo")

    def get_all_item_prices(self):
        price_elements = self.page.locator(".inventory_item_price")
        prices = price_elements.all_inner_texts()
        return [float(p.replace("$", "")) for p in prices]
    
    def get_item_names(self):
        elements = self.page.locator(".inventory_item_name")
        return elements.all_inner_texts()

    def sort_items_AtoZ(self):
        self.page.locator('.product_sort_container').click()
        self.page.locator('.product_sort_container').select_option("az")

    def sort_items_ZtoA(self):
        self.page.locator('.product_sort_container').click()
        self.page.locator('.product_sort_container').select_option("za")

