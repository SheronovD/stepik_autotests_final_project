from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
	REGISTER_LOGIN = (By.CSS_SELECTOR, "#id_registration-email")
	REGISTER_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
	REGISTER_PASS_CONF = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTER_BTN = (By.CSS_SELECTOR, "#register_form button")


class ProductPageLocators():
	ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form > button")
	PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p")
	PRODUCT_ADDED_MSG = (By.CSS_SELECTOR, "#messages div:nth-child(1) div strong")
	BASKET_TOTAL = (By.CSS_SELECTOR, "#messages div:nth-child(3) div strong")


class BasketPageLocators():
	BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
	EMPTY_BASKET_MSG = (By.CSS_SELECTOR, "#content_inner p")