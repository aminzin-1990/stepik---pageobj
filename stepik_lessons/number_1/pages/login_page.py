from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        register_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        register_email.send_keys(email)
        register_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        register_password.send_keys(password)
        register_password_confirm = self.browser.find_element(
            *LoginPageLocators.PASSWORD_CONFIRM)
        register_password_confirm.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_LINK), "Registration link is not presented"
