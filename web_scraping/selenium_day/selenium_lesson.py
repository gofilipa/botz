# coding: utf-8

### INTRODUCTION TO SELENIUM

# bs4 won't work
import requests
from bs4 import BeautifulSoup
import lxml
soup = BeautifulSoup(requests.get('https://doge.gov/').content, 'lxml')
soup.title

# niether will scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
response = HtmlResponse(url="https://doge.gov", body=body, encoding="utf-8")
response = HtmlResponse(url="https://doge.gov", encoding="utf-8")
response.css('title::text').get()
response.css('title')

### to install selenium

# run one of the following in your command line:
# conda install selenium
# pip install selenium

### to install driver:

# first, check your version of google chrome (open the app, select
# "chrome" at the top then "about chrome". Make a note of the first
# three numbers in the version.
# second, install the relevant /chromedriver/ from this page:
# https://googlechromelabs.github.io/chrome-for-testing/
# check "about this mac" to find out if you need arm64 (M1+ / apple
# sillicon chip) or x64 (intel chip).
# finally, once you download the file, unzip it, and move the folder to the
# same directory as the one you generally use for this class
# (containing your python files). 

### using selenium:

# imports: driver, service, by
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# variables to scrape site
url = 'https://doge.gov/'
d_path = '../chromedriver-mac-arm64/chromedriver'
service = Service(executable_path=d_path)
driver = webdriver.Chrome(service = service)

# scrape site
driver.get(url)

### our goal: to get the text from each post. check
### inspector for element for each post: for me, it is:
### div.border-2

# scraping element using "find_element" function, which takes two arguments
card = driver.find_element(By.CSS_SELECTOR, "div.border-2")

# see the card and just the text
card
card.text

# multiple elements with find_elements
cards = driver.find_elements(By.CSS_SELECTOR, "div.border-2")
cards
    
for i in cards:
    print(i.text)
    
