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
get_ipython().run_line_magic('save', 'adf_articles_bs4')
titles = []
blurbs = []
for i in range(1, 33):
    print(i)
    
for i in range(2, 34):
    print(i)
    
for i in range(2, 35):
    print(i)
    
titles
for i in range(2, 35):
    url = f'https://adflegal.org/articles/must-read/?pg={}'
for i in range(2, 35):
    url = f'https://adflegal.org/articles/must-read/?pg={}'
for i in range(2, 35):
    url = f'https://adflegal.org/articles/must-read/?pg={i}'
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    for i in soup.find_all('div', class_ = 'card-title')
for i in range(2, 35):
    url = f'https://adflegal.org/articles/must-read/?pg={i}'
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    for i in soup.find_all('div', class_ = 'card-title'):
        titles.append(i.text)
    for i in soup.find_all('div', class_ = 'card-text'):
        summaries.append(i.text)
        
    
summaries = []
for i in range(2, 35):
    url = f'https://adflegal.org/articles/must-read/?pg={i}'
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    for i in soup.find_all('div', class_ = 'card-title'):
        titles.append(i.text)
    for i in soup.find_all('div', class_ = 'card-text'):
        summaries.append(i.text)
        
titles
lent(titles)
len(titles)
for i in range(2, 35):
    url = f'https://adflegal.org/articles/must-read/?pg={i}'
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    for i in soup.find_all('div', class_ = 'card-title'):
        titles.append(i.text)
    for i in soup.find_all('div', class_ = 'card-text'):
        summaries.append(i.text)
    sleep(2)
    
import time
for i in range(2, 35):
    url = f'https://adflegal.org/articles/must-read/?pg={i}'
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    for i in soup.find_all('div', class_ = 'card-title'):
        titles.append(i.text)
    for i in soup.find_all('div', class_ = 'card-text'):
        summaries.append(i.text)
    sleep(2)
    
from time import sleep
for i in range(2, 35):
    url = f'https://adflegal.org/articles/must-read/?pg={i}'
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    for i in soup.find_all('div', class_ = 'card-title'):
        titles.append(i.text)
    for i in soup.find_all('div', class_ = 'card-text'):
        summaries.append(i.text)
    sleep(2)
    
len(summaries)
for i in range(2, 35):
    url = f'https://adflegal.org/articles/must-read/?pg={i}'
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    for i in soup.find_all('div', class_ = 'card-title'):
        titles.append(i.text)
    for i in soup.find_all('div', class_ = 'card-text'):
        summaries.append(i.text)
    print(titles)
    sleep(2)
    
titles = []
summaries = []
for i in range(2, 10):
    url = f'https://adflegal.org/articles/must-read/?pg={i}'
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    for i in soup.find_all('div', class_ = 'card-title'):
        titles.append(i.text)
    for i in soup.find_all('div', class_ = 'card-text'):
        summaries.append(i.text)
    print(titles)
    sleep(2)
    
for i in range(2, 10):
    url = f'https://adflegal.org/articles/must-read/?pg={i}'
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    print(soup.title)
    
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
for i in range(2, 10):
    url = f'https://adflegal.org/articles/must-read/?pg={i}'
    soup = BeautifulSoup(requests.get(url, headers=headers).content, 'lxml')
    print(soup.title)
    
proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}
for i in range(2, 10):
    url = f'https://adflegal.org/articles/must-read/?pg={i}'
    soup = BeautifulSoup(requests.get(url, headers=headers, proxies=proxies).content, 'lxml')
    print(soup.title)
    
for i in range(2, 10):
    url = f'https://adflegal.org/articles/must-read/?pg={i}'
    soup = BeautifulSoup(requests.get(url, headers=headers, proxies=proxies).content, 'lxml')
    print(soup.title)
    
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'http://google.com'
}
for i in range(2, 10):
    url = f'https://adflegal.org/articles/must-read/?pg={i}'
    soup = BeautifulSoup(requests.get(url, headers=headers).content, 'lxml')
    print(soup.title)
    
