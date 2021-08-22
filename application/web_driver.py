import os
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()


class WebDriver:

    @staticmethod
    def init_browser():
        return webdriver.Firefox()


class WebDriverManager(WebDriver):
    browser = None
    last_uuid = None
    url = str(os.environ.get('URL'))

    def open_browser(self):
        self.browser = self.init_browser()
        self.browser.get(self.url)

    def uuid_is_alive(self, uuid):
        return self.last_uuid == uuid



