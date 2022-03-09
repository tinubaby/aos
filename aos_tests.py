import unittest
import aos_locators as locators
import aos_methods as methods

class AosAppPositiveTestCases(unittest.TestCase):

    @staticmethod # signal to unittest that it is a static method
    def test_create_new_user():
        methods.setUp()
        methods.create_account()
        methods.logout()
        methods.login()
        methods.logout()
        methods.tearDown()
