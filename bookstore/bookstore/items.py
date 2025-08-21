import scrapy
class BookstoreItem(scrapy.Item):
    bookname=scrapy.Field()
    price=scrapy.Field()
    available=scrapy.Field()
    
