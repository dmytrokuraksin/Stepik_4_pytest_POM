from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    Basket_link = (By.CSS_SELECTOR, "span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    Basket_items = (By.CSS_SELECTOR, ".basket-items")
    Basket_is_empty_text = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")
    email = (By.CSS_SELECTOR, "#id_registration-email")
    password = (By.CSS_SELECTOR, "#id_registration-password1")
    confirm = (By.CSS_SELECTOR, "#id_registration-password2")
    registration_button = (By.XPATH, "//button [@name='registration_submit']")

class ProductPageLocators():
    add_to_cart = (By.CSS_SELECTOR, ".btn-add-to-basket")
    product_name = (By.CSS_SELECTOR, ".product_main h1")
    product_price = (By.CSS_SELECTOR, ".product_main .price_color")
    product_name_result = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div strong")
    product_price_result = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")