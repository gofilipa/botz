### class notes, intro to scrapy shell & starting spider

### websites to scrape:
# http://www.tm-research-archive.ch/
# https://hiring.cafe/
# https://lu.ma/user/accentaccent
# https://www.literature-map.com/
# https://www.theinfatuation.com
# https://plato.stanford.edu/


### to open a scrapy shell, type "scrapy shell 'https:your_url.com'"
### into the command line.

### some syntax for extracting html elements by classes

# to the the whole element
response.css('title')

# use ::text and get() to get just the text
response.css('title::text').get()
response.css('h1.image-hero__headline::text').get()

# take out leading and trailing white space
response.css('h1.image-hero__headline::text').get().strip()

# get all elements
response.css('h4.view-list--header::text').getall()

# get links using a::attr('href')
response.css('h1 a::attr('href')').get()

### challenge:
# get the headline, author, and link from each article
# 1. write a loop that isolates the parent element which
#    encapsulates all the information you want from the article.
# 2. isolate each element you want using .get()
###

for i in response.css("div.view-list--content-container"):
    print(i.css("h4::text").get())
    print(i.css("p.view-list--byline::text").get())

### To start a scrapy project & create a spider:
# 1. run "scrapy startproject project_name" in the 
#    command line
# 2. copy and paste starter code from scrapy docs,
#    on the "scrapy at a glance" page, paste into new
#    python script
# 3. save the python file to your project's "spiders" 
#    folder
# 4. on the script, change the variables and selectors 
#    to match your project
# 5. run the spider with the command:
#    "spacy crawl spider_name"
###
