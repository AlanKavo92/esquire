import random
from selenium import webdriver
from fashion_tap_lib import maximise_screen, login, top__users, follow_latest_users


driver = webdriver.Firefox()
maximise_screen(driver)
login(driver, 'esquire', 'equinox')

while True:
    random.shuffle(top__users)
    follow_latest_users(driver, 5000)
