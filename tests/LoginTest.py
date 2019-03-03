from SeleniumWDTests.pages.LoginPage import LoginPage
from SeleniumWDTests.config.config import config
from SeleniumWDTests.utils.base_testcase import BaseTestCase
import unittest

class TestLogin(BaseTestCase,LoginPage):
    webURL = config["login_url"]

    def setUp(self):
        print("TC level setup")
        self.launchLoginPage()

    def tearDown(self):
        print("TC level teardown")
        self.closeBrowser()

    def testLoginvalid(self):
        """
        Perform valid login Test
        :return:
        """
        self.loginUser()
        self.customWait()

if __name__== '__main__':
    unittest.main()