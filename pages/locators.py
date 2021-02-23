from selenium.webdriver.common.by import By

class BasketPageLocators():
    SHOPPING_LINK = (By.CSS_SELECTOR, "#content_inner>p>a")
    SHOPPING_FORM = (By.CSS_SELECTOR, "#content_inner>form")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BUTTON_LINK = (By.CSS_SELECTOR, "span.btn-group > a.btn-default")
    

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"] ')

class ProductPageLocators():

    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
##    BOOK_ADDED =  (By.CSS_SELECTOR, "div.alertinner > strong")
    BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6>h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.col-sm-6>p.price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div.alertinner >p>strong")
    SUCSESS_MSG = (By.CSS_SELECTOR," div.alert-success:first-child>div>strong")
    
    
    



