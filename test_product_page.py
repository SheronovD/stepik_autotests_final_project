import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('offer_num', ["1","2","3","4","5","6",pytest.param("7", marks=pytest.mark.xfail),"8","9"])
def test_guest_can_add_product_to_basket(offer_num, browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + offer_num
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_equal_name_with_added_product()
    page.should_be_equal_basket_total_with_added_product()
