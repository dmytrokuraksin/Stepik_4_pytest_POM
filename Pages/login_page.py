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