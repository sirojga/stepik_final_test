from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    

    def should_add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        try:
            self.solve_quiz_and_get_code()
        except Exception as e:
            print(str(e))     
        self.should_price_be_the_same()
        self.should_name_be_the_same()               
            
    def should_price_be_the_same(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text==self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text , "price is not the same"

    def should_name_be_the_same(self):
        assert self.browser.find_element(*ProductPageLocators.SUCSESS_MSG).text==self.browser.find_element(*ProductPageLocators.BOOK_NAME).text, "name is not the same" 

    def should_guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        assert self.is_not_element_present(*ProductPageLocators.SUCSESS_MSG), "message is present"

    def should_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCSESS_MSG), "message is present"
        
    def should_message_disappeared_after_adding_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        assert self.is_disappeared(*ProductPageLocators.SUCSESS_MSG), "message still present"
         

    
