import scrapy

from books.items import BooksItem

class BookSpider(scrapy.Spider):
    # name of the spider
    name = "book"
    # allowed domains to scrape, as well as where to start
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]


    # parse method to extract data: url, title, and price
    def parse(self, response):
        for book in response.css("article.product_pod"):
            item = BooksItem()
            item["url"] = book.css("h3 a::attr(href)").get()
            item["title"] = book.css("h3 a::attr(title)").get()
            item["price"] = book.css("p.price_color::text").get()
            yield item

    # need to be able to handle pagination, basically iterating through the pages on the webpage

        next_page = response.css("li.next > a::attr(href)").get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url = next_page_url, callback=self.parse)

        