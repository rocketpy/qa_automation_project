class Page(object):
    html = "html"
    ok_button = "#ok"
    cancel_button = "#cancel"
    see_items_button = "button.items"


class HomePage(object):
    see_items_button = "button.items"


class ShoppingPage(object):
    buyable_item = 'img[alt="Item"]'
    add_to_cart = "button.add"
    go_to_checkout = "#checkout"


class CheckoutPage(object):
    remove_from_cart = "button.remove"
    buy_now = "#buy-now"
    shop_more = "#shop-more"
    
    
#  in test file add this :
from base_test_case import BaseTestCase
from page_objects import HomePage, ShoppingPage, CheckoutPage


class MyTests(BaseTestCase):
    def test_example(self):
        self.login()
        self.click(HomePage.see_items_button)
        self.click(ShoppingPage.buyable_item)
        self.click(ShoppingPage.add_to_cart)
        self.click(CheckoutPage.buy_now)
        self.assert_element("#success")
        self.assert_text("Order Received!", "#h2")
