# BaseTestCase will inherit SeleniumBase methods from BaseCase
# with Python 3, simplify "super(...)" to super().setUp() and super().tearDown()

from seleniumbase import BaseCase


class BaseTestCase(BaseCase):

    def setUp(self):
        super(BaseTestCase, self).setUp()
        # run custom setUp() code for tests AFTER the super().setUp()

    def tearDown(self):
        self.save_teardown_screenshot()
        if self.has_exception():
            # run custom code if the test failed
            pass
        else:
            # run custom code if the test passed
            pass
        #  wrap unreliable tearDown() code in a try/except block
        #  run custom tearDown() code BEFORE the super().tearDown() 
        super(BaseTestCase, self).tearDown()

    def login(self):
        # Add code here
        # reduce duplicate code in tests by having reusable methods like this.
        # if the UI changes, the fix can be applied in one place.
        pass

    def example_method(self):
        # Add code here
        pass


'''
# now we can do something like this in test files:

from base_test_case import BaseTestCase


class MyTests(BaseTestCase):
    def test_example(self):
        self.login()
        self.example_method()
'''

