from selenium import webdriver
import chromedriver_binary

# open a Google Chrome page  # this is for Windows systems
browser = webdriver.Chrome()
browser.get('https://www.google.com')

# browser = webdriver.Firefox()  # this is for macos systems
#browser.get('https://www.google.com')
