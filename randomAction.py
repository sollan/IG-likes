from selenium import webdriver
import time
import re
from urllib.request import urlopen
import numpy as np
import selenium
import random


def goToHomePage(driver):
    buttons = driver.find_elements_by_class_name('Fifk5')
    buttons[0].click()
    time.sleep(random.randint(2,4))

def goToExplore(driver):
    buttons = driver.find_elements_by_class_name('Fifk5')
    buttons[1].click()
    time.sleep(random.randint(2,4))

def clickActivityButton(driver):
    buttons = driver.find_elements_by_class_name('Fifk5')
    buttons[2].click()
    time.sleep(random.randint(2,4))

def likeMoreOfThisUser(driver):
    posts = driver.find_elements_by_class_name('eLAPa')
    posts[random.randint(1,6)].click()
    time.sleep(3)
    buttons = driver.find_element_by_class_name('wpO6b ')
    like_button = buttons[0]
    time.sleep(1)
    like_button.click()
    time.sleep(random.randint(2,4))

# def clickCommentButton(driver):
#     buttons = driver.find_elements_by_class_name('wp06b  ')
#     comment_button = buttons.find_element_by_xpath("//svg[@aria-label='Comment']")
#     comment_button.click()
#     time.sleep(random.randint(2,4))

def savePost(driver):
    buttons = driver.find_elements_by_class_name('wpO6b ')
    save_button = buttons[3]
    save_button.click()
    time.sleep(random.randint(2,4))

# weights = [50, 10, 10, 30, 2]
functions = [
    # goToHomePage*weights[0], 
    # goToExplore*weights[1], 
    # clickActivityButton*weights[2], 
    # likeMoreOfThisUser*weights[3], 
    # savePost*weights[4]
    goToExplore, 
    clickActivityButton,
    goToExplore, 
    clickActivityButton,
    goToExplore, 
    clickActivityButton,
    goToHomePage, 
    goToExplore, 
    clickActivityButton,
    likeMoreOfThisUser, 
    savePost
    ]

# homepageWeights = [58, 12, 30]
homepageFunctions = [
    # goToHomePage*homepageWeights[0], 
    # goToExplore*homepageWeights[1], 
    # clickActivityButton*homepageWeights[2]
    goToHomePage, 
    goToExplore, 
    clickActivityButton,
    goToExplore, 
    clickActivityButton,
    goToExplore, 
    clickActivityButton,
    ]

def randomAction(driver):
    random.choice(functions)(driver)

def homepageRandomAction(driver):
    random.choice(homepageFunctions)(driver)