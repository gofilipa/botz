import scrapy

class GenderSpider(scrapy.Spider):
    name = "gender"
    start_urls = [
        "https://www.heritage.org/gender?f%5B0%5D=content_type%3Acommentary",
    ]

    def parse(self, response):
        article_page_links = response.css("div.result-card__info-wrapper a::attr('href')")
        yield from response.follow_all(article_page_links, self.parse_article)

        next_page = response.css('li.pager__item a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        yield {
            'title': response.css('h1.headline::text').get(),
            'takeaways':response.css('div.key-takeaways__takeaway p::text').getall(),
            'text': response.css('div.article__body-copy div p::text').getall()
        }
