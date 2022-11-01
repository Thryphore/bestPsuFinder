import scrapy
from ..items import AmazonscraperItem

class AmazonBotSpider(scrapy.Spider):
    name = 'amazon-bot'
    #for loop?
    count=1
    start_urls = ['https://www.amazon.com/s?k=PSU']

    def parse(self, response):
        product = AmazonscraperItem()

        name = response.css(".a-size-medium.a-text-normal::text").extract()
        product["name"]=name
        yield product
        AmazonBotSpider.count+=1
        nxt_page='https://www.amazon.com/s?k=PSU&page='+str(AmazonBotSpider.count)
        if AmazonBotSpider.count<6:
            yield response.follow(nxt_page,callback=self.parse)
        
