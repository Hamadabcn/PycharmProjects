import bs4
import requests

res = requests.get('https://es.wikipedia.org/wiki/Main_Page')

print(res.text)

noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

print(type(noStarchSoup))

element = noStarchSoup.select('#main-tfa > p:nth-child(4)')  # .select selects a specific part of the html page

print(element)

# what if we want only the text not the rest of the elements
print(element[0].getText())  # this will get only the text
