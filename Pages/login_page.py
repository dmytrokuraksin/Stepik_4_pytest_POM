import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is not in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "login_form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), "register_form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.email)
        email_input.send_keys(email)
        pass_input = self.browser.find_element(*LoginPageLocators.password)
        pass_input.send_keys(password)
        conf_input = self.browser.find_element(*LoginPageLocators.confirm)
        conf_input.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.registration_button)
        reg_button.click()
