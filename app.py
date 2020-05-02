from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
from follower import *

webdriver = webdriver.Chrome("C:/ChromeDriver/chromedriver.exe")
sleep(randint(2,4))
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(randint(3,4))

username = webdriver.find_element_by_name('username')
username.send_keys('towncarpacific@gmail.com')
password = webdriver.find_element_by_name('password')
password.send_keys('444peace')


#login click

webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button').click()
sleep(randint(4,5))


#notification pass

webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm').click()

hashtag_list = ['travelblog']
firstNProfile=10
commentAndFollow(webdriver, firstNProfile, hashtag_list)
