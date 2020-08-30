import math
import pytest
from pages.main_page import MainPage
from pages.base_page import BasePage
from .pages.login_page import LoginPage
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
    
"""
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
"""
