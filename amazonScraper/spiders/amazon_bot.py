import scrapy
from ..items import AmazonscraperItem

class AmazonBotSpider(scrapy.Spider):
    name = 'amazonBot'
    count=1
    start_urls = ['https://www.amazon.com/s?k=Computer+Power+Supply']

    def parse(self, response):
        product = AmazonscraperItem()

        name = response.css(".a-size-medium.a-text-normal::text").extract()
        price=response.css(".sg-col-12-of-20 .a-price-whole::text").extract()
        product["page"]=name
        product["price"]= price
        

        yield product
        AmazonBotSpider.count+=1
        nxt_page='https://www.amazon.com/s?k=Computer+Power+Supply'+str(AmazonBotSpider.count)
        if AmazonBotSpider.count<11:
            yield response.follow(nxt_page,callback=self.parse)
        
