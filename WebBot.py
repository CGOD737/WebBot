#WebBot Framework that can be configured for different automated Web Task

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Temporarily stores login information to use later on in the class.

#Actual Class
class WebBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("site.com")

    def accept_cookies(self):
        button = self.driver.find_element_by_id("privacy-layer-accept-all-button")
        button.click()

    def login(self, username, password):
        self.driver.get("site.com")
        email_input = self.driver.find_element_by_id("mms-login-form__email")
        email_input.clear()
        email_input.send_keys(username)
        pass_input = self.driver.find_element_by_id("mms-login-form__password")
        pass_input.clear()
        pass_input.send_keys(password)
        self.driver.find_element_by_id("mms-login-form__login-button").click()


if __name__ == "__main__":
    WebBot = WebBot()

    account = "username"
    password = "password"

    WebBot.login(account, password)
