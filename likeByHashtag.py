from bs4 import BeautifulSoup as bs
import time
import re
from urllib.request import urlopen
import json
from pandas.io.json import json_normalize
import pandas as pd, numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import random
from randomAction import *
from login import login
from likePost import *


with open("hashtags.json","r") as f:
    tags = json.load(f)

random.shuffle(tags)

browser = webdriver.Chrome('/home/annette/usr/chromedriver')
browser.get('https://www.instagram.com/')

login(browser)

try:
    # turn on notification?
    elem = browser.find_element_by_class_name('mt3GC')
    button = elem.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
    button.click()
    time.sleep(4)
except: 
    # verification needed
    input("Manual verification; press any key when done") 
    elem = browser.find_element_by_class_name('mt3GC')
    button = elem.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
    button.click()
    time.sleep(4)

# initialize working files
links = []
hashtag = []
num_liked = 0

# initialize save files
liked = []
liked_hashtag = []
when = []


for tag in tags:
    
    scroll = random.choices([0, 1])

    if scroll == [1]:

        browser.get('https://www.instagram.com/explore/tags/' + tag)
        for i in range(5):
            Pagelength = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
            # time.sleep(5)

        elements = browser.find_elements_by_class_name('eLAPa')

        # like recent posts
        for i in range(9, len(elements)):
            like = random.choices([0,1])
            if like == [1]:
                try:
                    clickPost(browser, i)
                    if manyLikes(browser):
                        # time.sleep(5)
                        time.sleep(3)
                        closePost(browser)
                        # time.sleep(4)
                        time.sleep(3)
                    else:
                        likePost(browser)
                        # time.sleep(10)
                        time.sleep(6)
                        # write to file
                        now = datetime.now()
                        now_string = now.strftime("%d-%m-%Y-%H-%M-%S")
                        when.append(now_string)
                        liked_hashtag.append(tag)
                        try:
                            reportBlockAction(browser)
                            print('blocked')
                            now = datetime.now()
                            now_string = now.strftime("%d-%m-%Y-%H-%M-%S")
                            df = pd.DataFrame(data={'link': liked, 'hashtag': liked_hashtag, 'when': when})
                            df.to_csv('./liked_' + now_string +'.csv', sep=',',index=False)
                            time.sleep(3000)
                        except:
                            closePost(browser)
                            # time.sleep(1)
                            posts = browser.find_elements_by_class_name('eLAPa')
                            link = posts[i].find_element_by_xpath('..').get_attribute('href')
                            liked.append(link)
                            print(link, tag, num_liked)
                            num_liked += 1
                except IndexError:
                    pass

                    
                

    # homepageRandomAction(browser)
    # time.sleep(15)
    time.sleep(8)

now = datetime.now()
now_string = now.strftime("%d-%m-%Y-%H-%M-%S")
df = pd.DataFrame(data={'link': liked, 'hashtag': liked_hashtag, 'when': when})
df.to_csv('./liked_' + now_string +'.csv', sep=',',index=False)