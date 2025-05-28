# coding: utf-8
from bs4 import BeautifulSoup
import requests
import lxml
soup = BeautifulSoup(requests.get('https://adflegal.org/articles/must-read/').content, 'lxml')
soup.title
# demonstrate how to use the inspector tool to find different parts
# demonstrate how to use the inspector tool to find different parts of the page
# use the find() function to search by element and class
soup.find('div', class_ = 'card-title')
# use the .text element to pull out just the text from the element
# use the .text element to pull out just the text from the element
# use the .text element to pull out just the text from the element
# use the .text element to pull out just the text from the element
soup.find('div', class_ = 'card-title').text
# use the find_all() method to get all of the headlines
headlines = soup.find_all('div', class_ = 'card-title')
headlines
for i in headlines:
    print(i.text)
    
titles = []
for i in headlines:
    titles.append(i.text)
    
titles
# challenge: use these tools to get the summary blurb for each article. 10-15 minutes & share.
