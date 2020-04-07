from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert len(self.browser.find_elements(*BasketPageLocators.BASKET_LINK)) == 0, "Basket is not empty"

    def should_be_basket_empty_message(self):
        assert 'Your basket is empty' in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text, \
            "Basket is not empty"

    def should_be_basket_empty_message(self):
        assert 'Your basket is empty' in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text, \
            "Basket is not empty"
