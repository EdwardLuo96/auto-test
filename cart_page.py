from .base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def verify_cart_items_count(self, expected_count):
        items = self.driver.find_elements(*self.CART_ITEMS)
        assert len(items) == expected_count

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)