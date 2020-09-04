import math
import pytest
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from selenium import webdriver


# pytest -s test_foo.py
# pytest -v --tb=line test_main_page.py

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_success_message(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()
    
@pytest.mark.xfail(reason="wrong message")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    #product_page.solve_quiz_and_get_code()
    #time.sleep(120)
    product_page.should_not_be_success_message()
    product_page.should_be_book_price()
    
@pytest.mark.xfail(reason="not disappiring")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.is_dissappeared()    
