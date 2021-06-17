from selenium import webdriver
from Internet_speed import InternetSpeedTwitterBot

promised_down = 150
promised_up = 10

chromedriver_path = "c:/Development/chromedriver"
ob_is = InternetSpeedTwitterBot()
ob_is.getspeed()
print(ob_is.down)
print(ob_is.up)

if ob_is.down<promised_down or ob_is.up <promised_up:
    ob_is.tweet()

