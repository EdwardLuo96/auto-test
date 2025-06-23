import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import tempfile


@pytest.fixture
def driver():
    temp_profile = tempfile.mkdtemp()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument(f"--user-data-dir={temp_profile}")
    chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_complete_purchase(driver):
    # 初始化页面对象
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 执行测试流程
    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    products_page.add_items_to_cart()
    products_page.go_to_cart()
    cart_page.verify_cart_items_count(2)
    cart_page.proceed_to_checkout()
    checkout_page.fill_shipping_info("Test", "User", "12345")
    total_price = checkout_page.finish_order()
    print(f"✅ 订单完成！总价: {total_price}")

# def test_basic_connection(driver):
#     """最基本的连接测试"""
#     print("\n正在执行基本连接测试...")
#     driver.get("https://www.google.com")
#     assert "Google" in driver.title
#     print("基本连接测试通过！")