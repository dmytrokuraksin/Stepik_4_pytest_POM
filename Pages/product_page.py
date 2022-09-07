from .base_page import BasePage
from .locators import ProductPageLocators

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

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.add_to_cart), "Add button is not presented"

    def testing_name_product(self, product_name):
        product_name_result = self.browser.find_element(*ProductPageLocators.product_name_result)
        assert product_name == product_name_result.text

    def testing_price_product(self, product_price):
        product_price_result = self.browser.find_element(*ProductPageLocators.product_price_result)
        assert product_price == product_price_result.text

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_not_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"