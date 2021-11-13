#WebBot Framework that can be configured for different automated Web Task

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

#Assuming chrome driver is in this location, change for whatever path you may have
PATH = "C:\Program Files (x86)\chromedriver.exe"

#Temporarily stores login information to use later on in the class.

#Actual Class
class WebBot:
    def __init__(self):
        print("WebBot is now intiating...")
        self.driver = webdriver.Chrome(PATH)
        
    def accept_cookies(self):
        button = self.driver.find_element_by_id("privacy-layer-accept-all-button")
        button.click()

    def login(self, username, password):
        self.driver.get("https://www.bestbuy.com/identity/signin?token=tid%3A47187327-44d5-11ec-8152-12a67a811cc3")
        email_input = self.driver.find_element_by_id("fld-e")
        email_input.clear()
        email_input.send_keys(username)
        pass_input = self.driver.find_element_by_id("fld-p1")
        pass_input.clear()
        pass_input.send_keys(password)
        time.sleep(10)


if __name__ == '__main__':

    WebBot = WebBot()

    account = "username"
    password = "password"

    WebBot.login(account, password)
