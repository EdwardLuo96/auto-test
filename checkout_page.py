from .base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_shipping_info(self, first_name, last_name, postal_code):
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_order(self):
        total_price = self.find(self.TOTAL_PRICE).text
        self.click(self.FINISH_BUTTON)
        self.wait_until_visible(self.COMPLETE_HEADER)
        assert "thank you" in self.find(self.COMPLETE_HEADER).text.lower()
        return total_price