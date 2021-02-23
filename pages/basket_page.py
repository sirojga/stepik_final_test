from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_guest_cant_see_product_in_basket_opened_from_product_page(self):
        self.basket_is_empty()
        self.empty_basket_text()
    
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.SHOPPING_FORM), "basket has product form"
    
    def empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.SHOPPING_LINK), "basket has product form"
