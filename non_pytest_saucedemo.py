from selenium import webdriver
# 打开百度
# def test_open_website():
#     driver = webdriver.Chrome()
#     driver.get("https://www.baidu.com")
#     assert "百度" in driver.title
#     driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import tempfile
import os

# 创建临时用户目录
temp_profile = tempfile.mkdtemp()

# 配置Chrome选项（终极方案）
chrome_options = Options()
chrome_options.add_argument("--incognito")  # 无痕模式不会保存密码
chrome_options.add_argument(f"--user-data-dir={temp_profile}")
chrome_options.add_argument("--password-store=basic")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "autofill.profile_enabled": False,
    "profile.default_content_setting_values.credentials_enable_service": False
})

driver = webdriver.Chrome(options=chrome_options)
try:
    driver.get("https://www.saucedemo.com/")

    # 登录前手动清除可能的缓存
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")

    # 1. 登录
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url
    print("✅ 登录成功")

    # 2. 添加商品
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    # 等待购物车徽章
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "2"
    print("✅ 商品已加入购物车")

    # 3. 进入购物车
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert "cart" in driver.current_url
    print("✅ 进入购物车页面")

    # 验证购物车商品数量
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 2, f"实际商品数量: {len(cart_items)}"
    print(f"✅ 购物车中有 {len(cart_items)} 件商品")

    # 4. 结算
    driver.find_element(By.ID, "checkout").click()
    assert "checkout-step-one" in driver.current_url
    print("✅ 进入结算页面")

    # 填写收货信息
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    assert "checkout-step-two" in driver.current_url
    print("✅ 填写收货信息成功")

    # 5. 完成订单
    total_price = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    driver.find_element(By.ID, "finish").click()

    # 验证订单完成（修正断言）
    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-complete")
    )
    complete_text = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "thank you for your order" in complete_text.lower()
    print(f"✅ 订单完成！总价: {total_price}")

except Exception as e:
    print("❌ 测试失败:", e)
    driver.save_screenshot("error.png")
finally:
    driver.quit()


# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from pages.login_page import LoginPage
# from pages.products_page import ProductsPage
# from pages.cart_page import CartPage
# from pages.checkout_page import CheckoutPage
# import tempfile
#
#
# @pytest.fixture
# def driver():
#     temp_profile = tempfile.mkdtemp()
#     chrome_options = Options()
#     chrome_options.add_argument("--incognito")
#     chrome_options.add_argument(f"--user-data-dir={temp_profile}")
#     chrome_options.add_argument("--disable-extensions")
#     driver = webdriver.Chrome(options=chrome_options)
#     yield driver
#     driver.quit()
#
# def test_complete_purchase(driver):
#     # 初始化页面对象
#     login_page = LoginPage(driver)
#     products_page = ProductsPage(driver)
#     cart_page = CartPage(driver)
#     checkout_page = CheckoutPage(driver)
#
#     # 执行测试流程
#     driver.get("https://www.saucedemo.com/")
#     login_page.login("standard_user", "secret_sauce")
#     products_page.add_items_to_cart()
#     products_page.go_to_cart()
#     cart_page.verify_cart_items_count(2)
#     cart_page.proceed_to_checkout()
#     checkout_page.fill_shipping_info("Test", "User", "12345")
#     total_price = checkout_page.finish_order()
#     print(f"✅ 订单完成！总价: {total_price}")

# def test_basic_connection(driver):
#     """最基本的连接测试"""
#     print("\n正在执行基本连接测试...")
#     driver.get("https://www.google.com")
#     assert "Google" in driver.title
#     print("基本连接测试通过！")