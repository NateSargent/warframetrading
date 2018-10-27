#augmods.py

import json
import time

import requests
from bs4 import BeautifulSoup

#http://warframe.wikia.com/wiki/Warframe_Augment_Mods
pveaugsurl = 'http://warframe.wikia.com/wiki/Warframe_Augment_Mods/PvE'
#marketbaseurl = 'https://warframe.market/items/'
marketbaseurl = 'https://api.warframe.market/v1/items/'
markettailurl = '/orders'

resp = requests.get(pveaugsurl)
html = resp.content
soup = BeautifulSoup(html, 'html.parser')

#mods = []
augdict = {}
for entry in soup.find_all('tr'):
    if not entry.find_all('a'):
        continue
    frame = entry.find_all('a')[1].text
    modsoup = entry.find_all('td')[1].find_all('a')
    factionsoup = entry.find_all('td')[2]
    mods = []
    for atag in modsoup:
        mods.append(atag.get('title'))
    augdict[frame] = mods

#for frame, mods in augdict.items():
#    for mod in mods:
#        mod_formatted = mod.lower().replace(' ', '_')
#        url = marketbaseurl + mod_formatted
#        print('url: ', url)
#        resp = requests.get(url)
#        market_page_dict = json.loads(resp.content)
#        orders = market_page_dict['payload']['orders']

def get_valid_orders(itemname):
    #itemname_formatted = itemname.lower().replace(' ', '_').replace('&', 'and')
    # lowercase
    itemname = itemname.lower()
    # replace spaces with underscores
    itemname = itemname.replace(' ', '_')
    # replace ampersand with 'and' (calm & frenzy)
    itemname = itemname.replace('&', 'and')
    # replace normal single quote (*'*, apostrophe, decimal 39) with special one
    # (*’*, unicode "right single quotation mark", dec 8217) (mesa's waltz)
    itemname = itemname.replace('\'', '’')
    url = marketbaseurl + itemname + markettailurl
    print('url: ', url)
    resp = requests.get(url)
    market_page_dict = json.loads(resp.json())
    orders = market_page_dict['payload']['orders']
    valid_orders = []
    for order in orders:
        # order is visible... maybe
        # order type is 'sell'
        if order['order_type'] != 'sell':
            #return False
            continue
        # order is on platform 'pc'
        if order['platform'] != 'pc':
            #return False
            continue
        # seller status is 'ingame'
        if order['user']['status'] != 'ingame':
            #return False
            continue
        # seller is in region 'en' (for "english", I guess, the other ones seem to be 'fr' and 'ru')
        if order['user']['region'] != 'en':
            #return False
            continue
        # you're good, I guess
        #return True
        valid_orders.append(order)
    return valid_orders

def average_five_lowest(item):
    valid_orders = get_valid_orders(item)
    prices = [order['platinum'] for order in valid_orders]
    prices.sort() # in-place
    fivelowest = prices[:5]
    average = sum(fivelowest)/len(fivelowest)
    return average
with open('augprices.txt', 'w') as f:
    for frame, mods in augdict.items():
        f.write('\n'+ frame + '\n')
        for mod in mods:
            average = average_five_lowest(mod)
            f.write(mod + ': ' + str(average) + '\n')
            time.sleep(1.5)


    