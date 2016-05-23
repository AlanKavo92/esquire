from selenium import webdriver
from fashion_tap_lib import set_screen_size, login, love_latest_photos


driver = webdriver.Firefox()
set_screen_size(driver, 200, 800)
login(driver, 'esquire', 'equinox')

love_latest_photos(driver)
