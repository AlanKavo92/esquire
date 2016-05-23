import time
import random
from selenium import webdriver
from fashion_tap_lib import maximise_screen, login, follow_users_followers, usernames, rndm


driver = webdriver.Firefox()
maximise_screen(driver)
login(driver, 'esquire', 'equinox')

follow_users_followers(driver, 'amy', 1, 10)
while True:
    random.shuffle(usernames)
    user = usernames.pop()
    time.sleep(rndm(5))
    follow_users_followers(driver, user, 1, 150)
