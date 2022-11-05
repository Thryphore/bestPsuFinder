import scrapy
from ..items import psuItem
from main import url

class PsuSpider(scrapy.Spider):
    name = 'psu'
    start_urls = ['https://www.amazon.com',url]

    def parse(self, response):
        product = psuItem()

        name = response.css("#productTitle::text").extract()
        product["itemName"]=name[0].strip()

        price = response.css("#corePriceDisplay_desktop_feature_div .a-price-whole::text").extract()
        product["price"]=price[0]

        yield product
