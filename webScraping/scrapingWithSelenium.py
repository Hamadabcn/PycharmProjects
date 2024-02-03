from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://en.wikipedia.org/wiki/Main_Page')

try:
    #elem = browser.find_element(By.CSS_SELECTOR, '#mp-tfa')   # this is find_element (brigs one element)
    #print(elem.text)

    # another exercise using find_elements (brings more than one element)
    elem = browser.find_elements(By.TAG_NAME, 'p')  # 'p' for paragraph
    print(len(elem))
    print(elem[0].text)

except:
    print('No element found')
