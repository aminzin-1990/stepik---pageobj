from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_MESSAGE =(By.CSS_SELECTOR, "#content_inner")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "[name='registration_submit'")

    EMAIL = (By.ID, "id_registration-email")
    PASSWORD = (By.ID, "id_registration-password1")
    PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-primary")


class ProductPageLocators:
    ADD_BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")

    ALERT_BOOK_ATTRIBUTE = (By.CSS_SELECTOR, ".alertinner")

    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, ".basket-mini")
