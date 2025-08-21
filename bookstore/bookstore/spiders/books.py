import scrapy
from bookstore.items import BookstoreItem
class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books=response.css('article.product_pod')
        for book in books:
          item = BookstoreItem()
          item['bookname'] = book.css('h3 a::attr(title)').get()
          item['price'] = book.css('p.price_color::text').get()
          item['available'] =item['available'] = ''.join(book.css('p.instock.availability::text').getall()).strip()
          yield item
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)