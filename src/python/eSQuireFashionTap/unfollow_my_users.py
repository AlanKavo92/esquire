from selenium import webdriver
from fashion_tap_lib import maximise_screen, login, unfollow_users_followers


driver = webdriver.Firefox()
maximise_screen(driver)
login(driver, 'esquire', 'equinox')

unfollow_users_followers(driver, 'esquire', 500, 8500)
