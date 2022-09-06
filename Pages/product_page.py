from .base_page import BasePage
from .locators import ProductPageLocators
import  time

class ProductPage(BasePage):

    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.add_to_cart)
        link.click()
        time.sleep(1)

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.add_to_cart), "Add button is not presented"