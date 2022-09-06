from .base_page import BasePage
from .locators import ProductPageLocators
import  time

class ProductPage(BasePage):

    def save_name_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.product_name)
        return product_name.text

    def save_price_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.product_price)
        return product_price.text

    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.add_to_cart)
        link.click()
        time.sleep(1)

    # def should_be_add_button(self):
    #     assert self.is_element_present(*ProductPageLocators.add_to_cart), "Add button is not presented"

    def testing_name_product(self, product_name):
        product_name_result = self.browser.find_element(*ProductPageLocators.product_name_result)
        assert product_name == product_name_result.text

    def testing_price_product(self, product_price):
        product_price_result = self.browser.find_element(*ProductPageLocators.product_price_result)
        assert product_price == product_price_result.text