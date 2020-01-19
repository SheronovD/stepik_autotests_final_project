from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
	ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form > button")
	PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p")
	PRODUCT_ADDED_MSG = (By.CSS_SELECTOR, "#messages div:nth-child(1) div strong")
	BASKET_TOTAL = (By.CSS_SELECTOR, "#messages div:nth-child(3) div strong")
