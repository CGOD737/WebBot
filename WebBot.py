#WebBot Framework that can be configured for different automated Web Task

from itertools import product
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
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

    #This Method is to be customized based on site information. Eventually will be a little more organized and user friendly
    def login(self, username, password, firstname, lastname):
        self.driver.get("https://www.walmart.com/account/login?vid=oaoh&ref=domain")
       
        email_input = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form[1]/div[1]/div/div[1]/input')
        email_input.clear()
        email_input.send_keys(username)
        
        pass_input = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form[1]/div[1]/div/div[2]/input')
        pass_input.clear()
        pass_input.send_keys(password)

        sign_in = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/form[1]/div[1]/div/button')
        sign_in.click()

        time.sleep(3)

        #click and hold security protocol
        element = self.driver.find_element_by_css_selector('#px-captcha')
        action = ActionChains(self.driver)
        click = ActionChains(self.driver)
        action.click_and_hold(element)
        action.perform()
        time.sleep(10)
        action.release(element)
        action.perform()
        time.sleep(0.2)
        action.release(element)

        time.sleep(20)

if __name__ == '__main__':

    WebBot = WebBot()

    account = "username"
    password = "password"

    WebBot.login(account, password)
