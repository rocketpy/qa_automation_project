import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    

"""
#  pytest -s -v test_file_name.py

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
"""

"""
#  for all class
@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        # this test will be run 2 times

    def test_guest_should_see_navbar_element(self, browser, language):
        # this test will be run 2 times
"""

# for use this fixture in file  test_file_name.py :
"""
link = "http://..."

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
"""
