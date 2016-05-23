import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException


top__users = ['dfmarin', 'jesslemos', 'shopbop', 'ariannamarie', 'being_apparel', 'flowactive',
              'damfino', 'slateandstone', 'ninecrows', 'jameswildexo', 'laserkitten', 'katiabyrne',
              'iamwissing', 'siostryohydki', 'freepeople', 'thehaberdashguy', 'imfinallyaunicorn',
              'bourgeoisboheme', 'molly', 'rhys.hobbins', 'oliverandthesea',  'fromsomeoneinlove',
              'kocoblaq', 'theoddportrait', 'labelsforlunch', 'sugarhighlovestoned', 'elvalexa',
              'echoandair', 'makeup', 'rebecca', 'lacemarieeyewear', 'midsommarswim', 'pennold',
              'daniellearce', 'leylita', 'katespadeny', 'howdoyouwearthat', 'tarinatarantino',
              'luanna90', 'shoptherunway', 'h.crowne', 'luccacouture', 'gregtbrown', 'blaklabel',
              'marissacydya', 'magic_fox', 'makeupgeekcosmetics', 'erika', 'mensstyle', 'katiepossage',
              'wildandfreejewelry', 'salientlabel', 'kristenxleanne', 'stormcalysta', 'gypsywarrior',
              'bellaandchloe', 'parkeryorksmith', 'apothecary87', 'ahitsrosa', 'itslikelymakeup',
              'pepaloves', 'laneandlanae', 'alittlelau', 'etoileboutique', 'oaknyc', 'tobi', 'hkassel',
              'limecrimemakeup', 'larsenthompson', 'avantvedge', 'chrisphelps', 'emilyruthroche',
              'missalissa', 'pinkperception', 'maggie_emerick', 'bedstu', '6shoreroadbypooja',
              'swedishhasbeens', 'outlinedcloth', 'vchillbruh', 'mytodayinstyle', 'graflantz',
              'imeltformakeup', 'daniella', 'sidewalk.stories', 'poletteeyewear', 'justauniform',
              'fashionkids', 'silvergirl', 'kyla_joy', 'nastygal', 'arcticfoxhaircolor', 'style',
              'brittanymatyas', 'amy', 'rackandclutch', 'hattiewatson', 'angl', 'celebritystyle',
              'ootd', 'mensweardaily', 'loveandleather']

global usernames
usernames = []

global total_follows
total_follows = 0

global hrefs
hrefs = []


def screen(msg):
    """
    Prints a message to the screen
    """
    print msg


def rndm(number_of_randoms):
    """
    Returns a random number between 0.00001 - 0.99999 * number_of_randoms
    """
    rng = 0
    for i in range(0, number_of_randoms):
        rng += random.random()

    return rng


def maximise_screen(driver):
    """
    Maximizes the webdriver window to the full screen ( Mac 13" )
    """
    screen('Maximizing screen size')

    driver.set_window_position(0, 0)
    driver.set_window_size(1280, 800)


def set_screen_size(driver, width, height):
    """
    Set the screen size in the webdriver window to the width/height passed ( Mac 13" )
    """
    screen('Setting screen size to: {0} [w] x {1} [h]'.format(width, height))

    driver.set_window_position(0, 0)
    driver.set_window_size(width, height)


def zoom_out(driver, zoom_percentage):
    """
    Unused !

    Might only work in chrome
    """
    screen('Setting zoom to: {0}'.format(zoom_percentage))

    driver.execute_script("document.body.style.zoom='{0}'".format(zoom_percentage))


def scroll(driver, scroll_size):
    """
    Scrolls the web page up or down

    +scroll_Size = up
    -scroll_size = down
    """
    driver.execute_script("window.scrollBy(0, {0});".format(scroll_size))


def scroll_to_end_of_page(driver):
    """
    Unused !

    Scrolls to the bottom of the browser
    """
    screen('Scrolling down to bottom of page')

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def write_to_file(_file, text):
    """
    Writes a piece of text to a file
    """
    with open(_file, 'a') as f:
        f.write('{0}\n'.format(text))


def read_file_into_list(_list, _file):
    """
    Reads contents of a file into memory
    """
    with open(_file, 'r') as f:
        for line in f:
            _list.append(line.strip())


def squash_file(file):
    """
    Removes duplicates from files
    """
    data = []
    with open(file, 'r') as f:
        for line in f:
            data.append(line)
    data = list(set(data))
    with open(file, 'w') as f:
        for d in data:
            f.write('{0}'.format(d))


def login(driver, username, password):
    """
    Logs ESQUIRE into fashiontap !
    """
    screen('Logging in')
    driver.get("http://fashiontap.com/login")

    username_element = WebDriverWait(driver, 10).until(lambda d: d.find_element_by_id('username'))
    password_element = WebDriverWait(driver, 10).until(lambda d: d.find_element_by_id('password'))
    username_element.clear()
    username_element.send_keys(username)
    password_element.clear()
    password_element.send_keys(password)

    login_button_element = WebDriverWait(driver, 10).until(lambda d: d.find_element(By.XPATH, '//button[text()="Sign In"]'))
    login_button_element.click()

    time.sleep(rndm(4))


def love_latest_photos(driver):
    """
    Loops over all the latest photos on the homepage and loves the photo !
    """
    screen('Liking latest photos on the homepage')

    driver.get('http://fashiontap.com/latest')
    time.sleep(rndm(3))

    href_xpath= '/html/body/main/section/div[2]/div/div/div[{0}]/div/a'

    index = 1
    counter = 0
    total_loved = 0
    refresh = True

    active_href_file = '../../../res/active_hrefs'
    active_user_file = '../../../res/active_users'

    squash_file(active_href_file)
    squash_file(active_user_file)

    global usernames
    global hrefs

    read_file_into_list(usernames, active_user_file)
    read_file_into_list(hrefs, active_href_file)

    while True:
        time.sleep(rndm(5))
        try:
            screen('Index: {0}'.format(index))
            link = driver.find_element(By.XPATH, href_xpath.format(index))
            href = link.get_attribute("href").split('/')[-1]

            user = link.get_attribute("href").split('/')[-2]
            if user not in usernames:
                usernames.append(user)
                write_to_file(active_user_file, user)

            screen('User: {0}\nPhoto ID: {1}'.format(user, href))

            if href in hrefs:
                screen('Skipping link!')
            else:
                hrefs.append(href)
                write_to_file(active_href_file, href)
                screen('Adding HREF to photos list!')

                link.click()
                refresh = True
                time.sleep(rndm(5))

                love_button_href = '/html/body/section/div/div/div[4]/a[1]'
                love = driver.find_element(By.XPATH, love_button_href)

                if 'btn-unlike' in love.get_attribute("class"):
                    screen('Photo already liked.. WHY WE HERE??!!')
                else:
                    screen('Loving photo!')
                    love.click()
                    total_loved += 1
                    screen('Total loves so far: {0}'.format(total_loved))
                    time.sleep(rndm(10))

                screen('Backkkk...!')
                driver.execute_script("window.history.go(-1)")

            index += 1
            counter += 1
            screen('Counter: {0}'.format(counter))
            if counter == 3:
                screen('Scrolling down: 139')
                scroll(driver, 139)
                counter = 0
                screen('Resetting counter')
                time.sleep(rndm(1))
        except WebDriverException:
            if refresh:
                driver.get('http://fashiontap.com/latest')
                refresh = False
                counter = 1
                index = 1
            scroll(driver, 127)


def unfollow_users_followers(driver, username, min_index=1, max_index=1000000):
    """
    Unfollows a users followers - accepts a start and finish index
    """
    screen('Unollowing {0}\'s followers'.format(username))

    driver.get('http://fashiontap.com/{0}/followings'.format(username))
    time.sleep(rndm(3))

    xpath = 'html/body/main/div[2]/div/div/div/div/div[{0}]/a[3]'
    index = 1
    cached_last_index = 0
    counter = 5
    total_unfollows = 0

    diff = [0, 0, 0, 0, 0, 0, 1]


    while True:
        try:
            if index < min_index:
                screen('Not at start index yet.. continuing! {0}/{1}'.format(index, min_index))
                index += 1
                scroll(driver, 80)
                continue

            if index == max_index:
                screen('Max index reached. Finishing! Total unfollowed: {0}'.format(total_unfollows))
                break

            if cached_last_index == index:
                scroll(driver, -100)
                continue

            follower = driver.find_element(By.XPATH, xpath.format(index + diff[counter]))

            if 'btn-follow' in follower.get_attribute("class"):
                screen('Follow button: Passssss')
            elif 'self' in follower.get_attribute("class"):
                screen('Edit button: Passssss')
                scroll(driver, 10)
            else:
                follower.click()
                total_unfollows += 1
                screen('Total unfollows so far: {0}'.format(total_unfollows))
                time.sleep(rndm(1))

            cached_last_index = index
            index += 1
            counter += 1
            if counter == 7:
                scroll(driver, 555)
                counter = 0
                diff = [0, 1, 2, 3, 4, 5, 6]
                random.shuffle(diff)
                time.sleep(rndm(1))
        except WebDriverException:
            counter = 1
            scroll(driver, -100)


def follow_users_followers(driver, username, min_index=1, max_index=1000000):
    """
    Follows a users followers
    """
    screen('Following {0}\'s followers'.format(username))

    driver.get('http://fashiontap.com/{0}/followers'.format(username))
    time.sleep(rndm(3))

    username_xpath = '/html/body/main/div[2]/div/div/div/div/div[{0}]/a[1]'
    button_xpath = 'html/body/main/div[2]/div/div/div/div/div[{0}]/a[3]'

    index = 1
    cached_last_index = 0
    counter = 5

    while True:
        try:
            if index < min_index:
                screen('Not at start index yet.. continuing! {0}/{1}'.format(index, min_index))
                index += 1
                scroll(driver, 80)
                continue

            if index == max_index:
                screen('Max index reached. Finishing! Total follows: {0}'.format(total_follows))
                break

            if cached_last_index == index:
                scroll(driver, -100)
                continue

            username = driver.find_element(By.XPATH, username_xpath.format(index)).get_attribute('href').split('/')[3]

            if username is not 'esquire':
                global usernames
                usernames.append(username)
                usernames = list(set(usernames))

            follower = driver.find_element(By.XPATH, button_xpath.format(index))

            if 'unfollow' in follower.get_attribute("class"):
                pass
            elif 'self' in follower.get_attribute("class"):
                pass
                scroll(driver, 10)
            else:
                follower.click()
                global total_follows
                total_follows += 1
                screen('Total follows so far: {0}'.format(total_follows))
                time.sleep(rndm(1))

            cached_last_index = index
            index += 1
            counter += 1
            if counter == 7:
                scroll(driver, 555)
                counter = 0
                time.sleep(rndm(1))
        except WebDriverException:
            #return
            counter = 1
            scroll(driver, -100)


def follow_latest_users(driver, max_index):
    """
    For every 'certified' user - check their latest followers and follow them
    """
    for user in top__users:
        time.sleep(rndm(30))
        screen('Total follows so far: {0}'.format(total_follows))
        follow_users_followers(driver, user, min_index=1, max_index=max_index)
