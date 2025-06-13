# Class notes, june 12

## overview

This is the last day of our unit on web scraping, will be moving on to social
media next unit.

Where we are:
- thinking about data we are interested in, not necessarily what we
  will do with that data (next week, text processing), but a general
  topic and/or resource is good.
- choosing a tool to get the data we want.
- after today will have 4 tools: bs4, scrapy, xhr, selenium.
- also after today, will have a sense of other projects that are
  already out there.

So we will start with a review of web scraping methods, then we will
move on to selenium.
- bs4 - good for scraping individual websites that are static
- scrapy - good for crawling websites, multiple pages, that are
  static.
  - framework, has a lot more functionality (such as processing data
    in sophisticated ways)
- xhr - good for getting dynamic data, by intercepting network
  requests.
- selenium - good for getting dynamic data by simulating a browser.

## intro to selenium

[Selenium](https://selenium-python.readthedocs.io) is a python library
for testing websites. It allows you to scrape dynamic content from
webpages, by creating a virtual (ghost-like) browser. 

### how to install selenium
- run one of the following in your command line

>  conda install selenium
>  pip install selenium

### how to install the chromedriver
- we must use a "chromedriver" for selenium -- creates a virtual
  browser for scraping.
- first, check your version of google chrome (open the app, select
  "chrome" at the top then "about chrome"). Make a note of the first
  three numbers in the version.
- then, install the relevant /chromedriver/ from this page:
  https://googlechromelabs.github.io/chrome-for-testing/
  - check "about this mac" to find out if you need arm64 (M1+ / apple
    sillicon chip) or x64 (intel chip).
  - other pages with more information and versions:-
    https://sites.google.com/chromium.org/driver/getting-started?authuser=0
    https://googlechromelabs.github.io/chrome-for-testing/files
- once you download the file, unzip it, and move the folder to the
  same directory as the one you generally use for this class
  (containing your python files). 

### selenium_lesson.ipynb

Now, open your preferred python notebook (jupyter or colab).

We will be scraping the doge.gov website. Notice that our usual
scrapers (`bs4` and `scrapy`) don't work, because they only work on
static sites. 

```python
  ### INTRODUCTION TO SELENIUM

  # notice that bs4 won't work
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

  # scrape site: after running this code, a virtual browser
  # should appear on your computer!
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

```

## environmental scan research

Spend some time researching projects and apps that relate to your
topic and/or your dataset. Create a list of 3-5 projects, considering
the following:
- projects should be some kind of data gathering and/or analysis of
  your chosen data or resource.
  - example: if you are scraping recipes, you might include a top
    recipe website, and/or an article that compares recipe websites.
- include at least two bots/scrapers. 
  - check both a search engine and github.com.
  - try searching "[your topic] scraper python", or "[your topic] bot
    python"

Once you have your projects chosen, go through them one by one and
answer the following questions:
- what the project does accomplish? what appears to be its strengths?
- what does the project not do, what is outside the scope of the
  project? Try to identify a gap that may be filled by futher work on
  the topic/dataset. 
- if the project uses python:
  - where is it getting its data from?
  - what python libraries is it using? (check "import" statements at
    the top of the python files).

## homework (due June 16): dataset brainstorm

What is the dataset you'd like to use as a basis for your final project? Where
would you get the data, and how would you go about collecting it?

Include a paragraph that explains your interest in the data, and
include a bulleted list with concrete steps for gathering the data.
