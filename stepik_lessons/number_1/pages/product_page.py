from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        add_to_basket_link.click()

    def should_be_after_pay(self):
        self.should_be_name_match()
        self.should_be_price_match()
        # self.should_not_be_success_message()
        # self.should_disappeared_of_success_message()

    def should_be_name_match(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text + ' has been added' in \
               self.browser.find_elements(*ProductPageLocators.ALERT_BOOK_ATTRIBUTE)[0].text, \
               "Book is not add to basket"

    def should_be_price_match(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text in \
               self.browser.find_element(*ProductPageLocators.TOTAL_BASKET_PRICE).text, "Price do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_BOOK_ATTRIBUTE), \
            "Success message is presented, but should not be"

    def should_disappeared_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_BOOK_ATTRIBUTE), \
            "Success message is visible, but should not be"

