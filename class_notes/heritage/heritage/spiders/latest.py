import scrapy

class LatestSpider(scrapy.Spider):
    name = "latest"
    start_urls = [
        "https://heritage.org",
    ]

    def parse(self, response):
        article_page_links = response.css("div.node__content a::attr('href')")
        yield from response.follow_all(article_page_links, self.parse_article)
    
    def parse_article(self, response):
        yield {
            'title': response.css('h1.commentary__headline::text').get(),
            'text': response.css('div.article__body-copy div p::text').getall()
        }