from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        add_to_basket_link.click()

    def should_be_after_pay(self):
        self.should_be_name_match()
        self.should_be_price_match()

    def should_be_name_match(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text + ' has been added' in \
               self.browser.find_elements(*ProductPageLocators.ALERT_BOOK_ATTRIBUTE)[0].text, \
               "Book is not add to basket"

    def should_be_price_match(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text in \
               self.browser.find_element(*ProductPageLocators.TOTAL_BASKET_PRICE).text, "Price do not match"

