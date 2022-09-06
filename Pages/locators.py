from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    add_to_cart = (By.CSS_SELECTOR, ".btn-add-to-basket")
    product_name = (By.CSS_SELECTOR, ".product_main h1")
    product_price = (By.CSS_SELECTOR, ".product_main .price_color")
    product_name_result = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div strong")
    product_price_result = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div strong")