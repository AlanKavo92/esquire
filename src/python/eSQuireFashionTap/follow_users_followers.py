from selenium import webdriver
from fashion_tap_lib import login, maximise_screen, follow_users_followers


driver = webdriver.Firefox()
maximise_screen(driver)
login(driver, 'esquire', 'equinox')

follow_users_followers(driver, 'amy', 1000, 25000)
