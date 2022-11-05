import os
import json
from psus import *

import time
start_time = time.time()

from amazonScraper.spiders.amazon_bot import AmazonBotSpider
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess(settings={
    "FEEDS": {
        "products.json": {"format": "json"},
    },
})

process.crawl(AmazonBotSpider)
process.start() # the script will block here until the crawling is finished

exit(0)


os.system("scrapy crawl amazonBot -O products.json")
with open('products.json', 'r') as f:
    psus = json.load(f)

print("")
print("Enter the maximum watts you want: ")
maxWatts = int(input())
print("__________________________________________________________________________________________________________________________________________________________________________")
print("")
print("")

def testItems(dict):
    for item in dict:
        url = item
        os.system("scrapy crawl psu -O psu.json")
        with open('psu.json', 'r') as f:
            psu = json.load(f)
        
        if any(x in item for x in ["""Bad power supply companies ->""" "aresgame", "pystar", "armageddon", "gamemax", "gamepower", "nox", "redragon", "jetek"
        """Filter for non-computer power supplies ->""", "adapter", "laptop", "raspberry pi", "backup", "camera", "mining", "comeap"]): #This may not be faster in the long term...
            continue

        if psuWattage(item) != None:
            if int(psuWattage(item)) >= maxWatts:
                continue
        
        if "evga" in item:
            EVGA(item)
            continue

        if "corsair" in item: 
            corsair(item)
            continue

for dict in psus:
    testItems(dict["page"])

printTierList()

print("Took this long to run: ", time.time() - start_time)