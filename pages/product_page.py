from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_equal_name_with_added_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        added_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MSG)
        assert product_name.text == added_product_name.text , "Wrong product added"

    def should_be_equal_basket_total_with_added_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        assert basket_total.text == product_price.text , "Wrong basket total result"