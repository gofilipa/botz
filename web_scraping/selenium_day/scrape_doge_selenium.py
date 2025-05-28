### install selenium with conda or pip
### install chromedriver by version, move to current directory

# imports: driver, service, by
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# variables to scrape site
url = 'https://doge.gov/'
d_path = './chromedriver-mac-arm64/chromedriver'
service = Service(executable_path=d_path)
driver = webdriver.Chrome(service = service)

# scrape site
driver.get(url)

### check inspector for element for each post: div.border-2

# scraping element using "find_element" function, which takes two
# arguments
card = driver.find_element(By.CSS_SELECTOR, "div.border-2")
card
card.text

# multiple elements with find_elements
cards = driver.find_elements(By.CSS_SELECTOR, "div.border-2")
cards

# get just the text
for i in cards:
    print(i.text)
len(cards)

### group challenge: write some code to extract the important
### information from these cards. you'll have to think about strategy:
### are you going to loop through the cards we already haveand take
### out the individual elements from each card, then save them to
### lists? Or will you re-scrape the content, specifically calling
### each item that we want?
