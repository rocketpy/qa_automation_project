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
