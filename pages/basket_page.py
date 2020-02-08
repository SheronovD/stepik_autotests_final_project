from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), \
        "Products in basket is presented, but should not be"

    def should_be_empty_basket_message(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MSG).text, \
        "Empty basket message is not presented"