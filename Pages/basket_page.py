from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def test_guest_cant_see_added_product(self):
        assert self.is_not_element_present(*BasketPageLocators.Basket_items), "Added product in cart"

    def test_message_cart_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.Basket_is_empty_text), "Div with text about empty cart"