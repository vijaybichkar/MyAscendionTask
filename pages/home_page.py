class HomePage:
    def __init__(self, page):
        self.page = page
        self.burger_menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")
        self.cart_button = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.product_titles = page.locator(".inventory_item_name")
        self.product_descriptions = page.locator(".inventory_item_desc")

    def logout(self):
        self.burger_menu_button.click()
        self.page.wait_for_timeout(500)
        self.logout_link.click()

    def add_item_to_cart(self):
        self.page.locator("button[id^='add-to-cart']").first.click()

    def remove_item_from_cart(self):
        self.page.locator("button[id^='remove']").first.click()

    def go_to_cart(self):
        self.cart_button.click()

    def get_cart_count(self):
        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content())
        return 0

    def sort_items_by_price_low_to_high(self):
        self.page.locator('.product_sort_container').select_option("lohi")

    def sort_items_by_price_high_to_low(self):
        self.page.locator('.product_sort_container').select_option("hilo")

    def sort_items_AtoZ(self):
        self.page.locator('.product_sort_container').select_option("az")

    def sort_items_ZtoA(self):
        self.page.locator('.product_sort_container').select_option("za")

    def get_all_item_prices(self):
        prices = self.page.locator(".inventory_item_price").all_inner_texts()
        return [float(p.replace("$", "")) for p in prices]

    def get_item_names(self):
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def extract_inventory_data(self):
        items = self.page.locator(".inventory_item")
        count = items.count()
        inventory_data = []

        for i in range(count):
            name = items.nth(i).locator(".inventory_item_name").inner_text()
            price = items.nth(i).locator(".inventory_item_price").inner_text().replace("$", "")
            button_text = items.nth(i).locator("button.btn_inventory").inner_text()
            image_src = items.nth(i).locator(".inventory_item_img img").get_attribute("src")

            inventory_data.append({
                "name": name,
                "price": float(price),
                "button": button_text,
                "image": image_src
            })

        return inventory_data
