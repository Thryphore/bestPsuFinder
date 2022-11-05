import scrapy
from ..items import AmazonscraperItem

class AmazonBotSpider(scrapy.Spider):
    name = 'amazonBot'
    count=1
    start_urls = ['https://www.amazon.com/s?k=Computer+Power+Supply']

    def parse(self, response):
        print("hi")
        product = AmazonscraperItem()

        name = response.css(".s-line-clamp-2").css("::attr(href)").extract()
        product["page"]=name
        

        yield product
        AmazonBotSpider.count+=1
        nxt_page='https://www.amazon.com/s?k=Computer+Power+Supply&page='+str(AmazonBotSpider.count)
        if AmazonBotSpider.count<11:
            yield response.follow(nxt_page,callback=self.parse)
        
