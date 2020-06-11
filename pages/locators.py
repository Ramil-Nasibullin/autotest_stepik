from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "input[name=registration-password1]")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "input[name=registration-password2]")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn .btn-default")


class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner") # "#basket_formset")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_PRODUCT_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    NAME_PRODUCT_BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")