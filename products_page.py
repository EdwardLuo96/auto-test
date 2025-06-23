from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductsPage(BasePage):
    ADD_BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKELIGHT_BTN = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_items_to_cart(self):
        self.click(self.ADD_BACKPACK_BTN)
        self.click(self.ADD_BIKELIGHT_BTN)
        self.wait_until_visible(self.CART_BADGE)
        assert self.find(self.CART_BADGE).text == "2"

    def go_to_cart(self):
        self.click(self.CART_LINK)