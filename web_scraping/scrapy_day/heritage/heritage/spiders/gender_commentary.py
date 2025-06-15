import scrapy

class GenderSpider(scrapy.Spider):
    name = "gender"
    start_urls = [
        "https://www.heritage.org/gender?f%5B0%5D=content_type%3Acommentary",
    ]

    # Get the links to the articles, pass them to parse_article 
    def parse(self, response):
        article_page_links = response.css("div.result-card__info-wrapper a::attr('href')")
        yield from response.follow_all(article_page_links, self.parse_article)

        # Go to the next page of results
        next_page = response.css('li.pager__item a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    # get the text from the individual articles
    def parse_article(self, response):

        # Try all possible selectors for author names (copilot)
        # Needed to get all of the authors, listed across different elements and classes
        authors_raw = (
            response.css('a.author-card__name span::text').getall() +
            response.css('p.author-card__name span::text').getall() +
            response.css('a.author-card__multi-name span::text').getall() +
            response.css('span.author-card__name span::text').getall()
        )
        # Flatten and clean the list (copilot)
        authors = [a.strip() for a in authors_raw if isinstance(a, str) and a.strip()]

        # getting text and links while keeping the structure (copilot)
        container = response.css('div div.article__body-copy div')
        elements = container.xpath('./p | ./a')
        content = []
        for el in elements:
            if el.root.tag == 'p':
                text = el.xpath('string()').get().strip()
                if text:
                    content.append(text)
            elif el.root.tag == 'a':
                text = el.xpath('string()').get().strip()
                href = el.xpath('./@href').get()
                if text and href:
                    content.append(f'<a href="{href}">{text}</a>')
        full_content = ' '.join(content)

        yield {
            'title': response.css('h1.headline::text').get(),
            'author': authors,
            'date': response.css('div.article-general-info::text').get(),
            'url': response.url,
            'takeaways':response.css('div.key-takeaways__takeaway p::text').getall(),
            'text': full_content
        }
