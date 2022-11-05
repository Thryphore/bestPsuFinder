# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonscraperItem(scrapy.Item):
    page = scrapy.Field()

class psuItem(scrapy.Item):
    itemName = scrapy.Field()
    price = scrapy.Field()