from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


# class MainPageLocators:
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "[name='registration_submit'")


class ProductPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")

    ALERT_BOOK_ATTRIBUTE = (By.CSS_SELECTOR, ".alertinner")

    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, ".basket-mini")
