from selenium import webdriver
from SeleniumWDTests.config.config import config
import time

class UiAutoUtil():
    _driverlocation = config["driver_chrome_path"]
    chromedriver = None

    def __init__(self):
        self.chromedriver = webdriver.Chrome(self._driverlocation)
        self.chromedriver.implicitly_wait(1)
        self.chromedriver.maximize_window()

    def launchPage(self,webURL):
        self.chromedriver.get(webURL)
        pageURL = self.chromedriver.current_url
        assert pageURL == webURL

    def customWait(self,timeout=3):
        time.sleep(timeout)

    def typeText(self,element,inputtext):
        element.clear()
        element.send_keys(inputtext)

    def clickElement(self, element):
        element.click()

    def closeBrowser(self):
        self.chromedriver.close()
