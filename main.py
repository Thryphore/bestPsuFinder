import os
import json
from psus import *

import time
start_time = time.time()

#os.system("cd amazonScraper")
#os.system("scrapy crawl amazonBot -O products.json")

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
        item = item.lower()

        if any(x in item for x in ["""Bad power supply companies""" "aresgame", "pystar", "armageddon", "gamemax", "gamepower", "nox", "redragon", "jetek"
        """Filter for non-computer power supplies""", "adapter", "laptop", "raspberry pi", "backup", "camera", "mining", "comeap"]): #This may not be faster in the long term...
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