from selenium import webdriver
chromedriver_path = "c:/Development/chromedriver"
speedtest_url = "https://www.speedtest.net/"
twitter_url = "https://twitter.com/"
twitter_email = "aryansri009@gmail.com"
twitter_password = "Password1234"
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path= chromedriver_path)
        self.down = 0
        self.up = 0

    def getspeed(self):
        self.driver.get(speedtest_url)
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        time.sleep(10)
        go_button.click()
        time.sleep(60)
        self.down = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.up = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
        time.sleep(2)

    def tweet(self):
        self.driver.get(twitter_url)
        time.sleep(5)
        log_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
        log_in.click()
        time.sleep(3)
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email.send_keys(twitter_email)
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(twitter_password)
        password.send_keys(Keys.ENTER)
        time.sleep(10)
        message = f"Hey, Internet Provider why is my speed {self.down}down and {self.up}up?"
        placeholder = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div')
        placeholder.send_keys(message)
        time.sleep(10)
        