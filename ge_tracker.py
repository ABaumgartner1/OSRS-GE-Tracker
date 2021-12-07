# OSRS GE item scraper created by Aaron Baumgartner in 2021

import requests
import bs4

# hold the current urls for all items I want to track
item_urls = ["https://secure.runescape.com/m=itemdb_oldschool/Dragon+hunter+lance/viewitem?obj=22978", "https://secure.runescape.com/m=itemdb_oldschool/Bandos+chestplate/viewitem?obj=11832", 
"https://secure.runescape.com/m=itemdb_oldschool/Bandos+tassets/viewitem?obj=11834", "https://secure.runescape.com/m=itemdb_oldschool/Primordial+boots/viewitem?obj=13239", 
"https://secure.runescape.com/m=itemdb_oldschool/Amulet+of+torture/viewitem?obj=19553", "https://secure.runescape.com/m=itemdb_oldschool/Abyssal+whip/viewitem?obj=4151",
"https://secure.runescape.com/m=itemdb_oldschool/Armadyl+chestplate/viewitem?obj=11828", "https://secure.runescape.com/m=itemdb_oldschool/Armadyl+chainskirt/viewitem?obj=11830",
"https://secure.runescape.com/m=itemdb_oldschool/Toxic+blowpipe+%28empty%29/viewitem?obj=12924", "https://secure.runescape.com/m=itemdb_oldschool/Uncharged+toxic+trident/viewitem?obj=12900",
"https://secure.runescape.com/m=itemdb_oldschool/Necklace+of+anguish/viewitem?obj=19547", "https://secure.runescape.com/m=itemdb_oldschool/Spectral+spirit+shield/viewitem?obj=12821"]
rare_urls = ["https://secure.runescape.com/m=itemdb_oldschool/Scythe+of+vitur+%28uncharged%29/viewitem?obj=22486", "https://secure.runescape.com/m=itemdb_oldschool/Twisted+bow/viewitem?obj=20997"]
total = 0.0

# go to the url for an item and collect information (item name, current price, price change for today, 1 month change, 3 month change, and 6 month change)
def scrape_ge(url):
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text,"lxml")
    item = soup.select('h2')[0].getText()
    prices = [soup.select('span')[4].getText(),soup.select('span')[5].getText(),soup.select('span')[8].getText(),soup.select('span')[11].getText(),soup.select('span')[14].getText()]
    return item,prices,prices[0]

# display item info
def display_ge_info(item,prices):
    temp = []
    print(item)
    print("Price: " + prices[0])
    print("Today's change: " + prices[1])
    print("1 month change: " + prices[2])
    print("3 month change: " + prices[3])
    print("6 month change: " + prices[4])

# display information for all items that I currently own and display the total value at the end
for i in item_urls:
	item,prices,cur_price = scrape_ge(i)
	display_ge_info(item,prices)
	print()
	cur_price = cur_price[0:len(cur_price)-1]
	total = total + float(cur_price)

print("Total value: " + str(total) + "m")
print()

# display information for high value items or items that I want to track for flipping
for i in rare_urls:
	item,prices,cur_price = scrape_ge(i)
	display_ge_info(item,prices)
	print()
