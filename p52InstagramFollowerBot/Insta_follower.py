from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

chromedriver = "c:/Development/chromedriver"
username = "hi_aryan009"
password = "Prioryofsion08"
target_account = "meraki_poet"
url = "https://www.instagram.com/"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path= chromedriver)

    def login(self):
        self.driver.get(url)
        time.sleep(5)
        un = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        un.send_keys(username)
        pw = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        pw.send_keys(password)
        pw.send_keys(Keys.ENTER)

    def find_followers(self):
        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(target_account)
        time.sleep(3)
        search.send_keys(Keys.ENTER)
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(5)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(2000):
        #In this case we're executing some Javascript, that's what the execute_script() method does. 
        #The method can accept the script as well as a HTML element. 
        #The modal in this case, becomes the arguments[0] in the script.
        #Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            self.follow()
            time.sleep(3)
    
    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                time.sleep(1)
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()



