from SeleniumWDTests.utils.ui_auto_util import UiAutoUtil
from SeleniumWDTests.config.config import config

class LoginPage(UiAutoUtil):

    def get_user_id(self):
        return self.chromedriver.find_element_by_id("user_login")

    def get_user_pwd(self):
        return self.chromedriver.find_element_by_id("user_pass")

    def get_btn_signin(self):
        return self.chromedriver.find_element_by_id("wp-submit")

    def launchLoginPage(self):
        self.launchPage(config["login_url"])

    def loginUser(self):
        id_txt = self.get_user_id()
        pwd_txt = self.get_user_pwd()
        self.typeText(id_txt,config["user_id"])
        self.typeText(pwd_txt,config["user_pwd"])
        self.customWait()
        btnSignin = self.get_btn_signin()
        self.clickElement(btnSignin)
        self.customWait()