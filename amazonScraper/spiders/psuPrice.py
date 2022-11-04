#future implementation?
"""import scrapy
from ..items import AmazonscraperItem

class PsupriceSpider(scrapy.Spider):
    name = 'psuPrice'
    start_urls = ['https://www.amazon.com/s?k='+psuToSearch]

    def parse(self, response):
        product = AmazonscraperItem()

        price=response.css(".sg-col-12-of-20 .a-price-whole::text").extract()
        product["price"]= price

        yield product
"""