from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()  # this is to open the wikipedia's page
browser.get('https://en.wikipedia.org/wiki/Main_Page')

try:
    # click operator, this will click on a button on a page
    # elem = browser.find_element(By.CSS_SELECTOR, '#ca-viewsource > a > span')  # inspect the page then copy selector
    # elem.click()  # for the element to click on the button
    # time.sleep(5)  # delay time to see what is going on 5 seconds in this case

    # search operator, what if we want to search for something
    # elem = browser.find_element(By.CSS_SELECTOR, '#searchInput')  # copy selector from the page
    # elem.send_keys('Python')  # what to search for python in this case
    # time.sleep(3)
    #
    # # now that you what you want to search for press the search button
    # # that is how submit to the search button
    # button = browser.find_element(By.CSS_SELECTOR, '#searchform > div > button')
    # button.submit()
    # time.sleep(5)

    # scroll operator, first open the page
    time.sleep(3)  # wait for 3 seconds
    htmlElem = browser.find_element(By.TAG_NAME, 'html')
    htmlElem.send_keys(Keys.END)  # this will go to the end of the page
    time.sleep(3)  # wait for 3 seconds more
    htmlElem.send_keys(Keys.HOME)  # this will go to the top of the page
    time.sleep(3)  # wait for 3 seconds

    # selenium can do much more look at the documentation

except:
    print('No element found')
