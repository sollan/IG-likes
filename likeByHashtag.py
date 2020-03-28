from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import re
from urllib.request import urlopen
import json
from pandas.io.json import json_normalize
import pandas as pd, numpy as np
from selenium.webdriver.common.keys import Keys
import random

tags = ['']

login_data = {
    'username': '',
    'password': ''
}

browser = webdriver.Chrome('/path/to/chromedriver/')
browser.get('https://www.instagram.com/')

# log in

elem = browser.find_element_by_name('username')
elem.clear()
elem.send_keys(login_data['username'])
time.sleep(1)
elem = browser.find_element_by_name('password')
elem.send_keys(login_data['password'])
time.sleep(1)
elem.send_keys(Keys.ENTER)
time.sleep(7)

for tag in tags:
    links=[]
    browser.get('https://www.instagram.com/explore/tags/' + tag)

    for i in range(5):
        Pagelength = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    elements = browser.find_elements_by_class_name('eLAPa')
    for i in range(len(elements)):
        link = elements[i].find_element_by_xpath('..').get_attribute('href')
        if link not in links:
            links.append(link)

    for link in links:
        like = random.choices([0,1])
        if like == 1:
            browser.get(link)
            elem = browser.find_element_by_class_name('fr66n')
            elem.click()


