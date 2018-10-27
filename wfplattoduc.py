#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from bs4 import BeautifulSoup
#from beautifulsoup4 import BeautifulSoup
import subprocess
from ducat_prices import ducat_prices_dict

marketbaseurl = 'https://api.warframe.market/v1/items/'
markettailurl = '/orders?include=item'

# get ducat prices
dpd = ducat_prices_dict

#find 45 ducat item names
fortyfives = []
for item in dpd.items():
    if item[1] == '45':
        fortyfives.append(item[0])

# look at orders for the fortyfives
def get_valid_orders(itemname):
    itemname = format_item_name_for_market_url(itemname)
    url = marketbaseurl + itemname + markettailurl
    resp = requests.get(url)
    market_page_dict = resp.json()
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

def format_item_name_for_market_url(name):
    # handle prime part blueprints, e.g. "Ash Prime Neuroptics Blueprint" needs to be "ash_prime_neuroptics" and not "ash_prime_neuroptics_blueprint"
    if ((('Prime' in name) and ('Neuroptics' in name)) or
    (('Prime' in name) and ('Chassis' in name)) or
    (('Prime' in name) and ('Systems' in name))):
        name = name.replace(' Blueprint', '')
    # lowercase the letters
    name = name.lower()
    #replace spaces with underscores
    name = name.replace(' ', '_')
    # replace ampersands with 'and' (calm & frenzy, silva & aegis)
    name = name.replace('&', 'and')
    # replace normal single quote (*'*, apostrophe, decimal 39) with special one
    # (*’*, unicode "right single quotation mark", dec 8217) (mesa's waltz)
    name = name.replace('\'', '’')
    return name


def find_bulk(min_quantity=1, skips=0):
    candidate = None
    for item in fortyfives:
        print('trying item %s' % item)
        orders = get_valid_orders(item)
        # sort the orders
        orders = sorted(orders, key=lambda price: price.get('platinum'))
        #print(len(orders))
        if len(orders) < 1:
            continue
        for order in orders:
            if order['platinum'] > 4:
                break
            if order['quantity'] >= min_quantity:
                if skips > 0:
                    #print('skipping order by %s' % order['user']['ingame_name'])
                    skips -= 1
                    continue
                result_dict = {}
                result_dict['item'] = item
                result_dict['seller'] = order['user']['ingame_name']
                result_dict['price'] = order['platinum']
                result_dict['quantity'] = order['quantity']
                #print('candidate found: %s selling %s %s at %sp' % (order['user']['ingame_name'], order['quantity'], item, order['platinum']))
                #print('warframe market URL: https://warframe.market/items/%s' % format_item_name_for_market_url(item))
                result_dict['market_url'] = 'https://warframe.market/items/%s' % format_item_name_for_market_url(item)
                #chatmessage = '/w %s WTB %s at %sp, I\'ll take more than one' % (order['user']['ingame_name'], item, order['platinum'])
                result_dict['chatmessage'] = '/w %s WTB %s at %sp, I\'ll take more than one' % (order['user']['ingame_name'], item, order['platinum'])
                #print('chat message:')
                #print(chatmessage)
                #subprocess.call('echo %s | clip' % chatmessage, shell=True)
                return result_dict


# old code below
"""

def format_item_name_for_market_url(name):
    #return name.lower().replace(' ', '_')
    # handle prime part blueprints, e.g. "Ash Prime Neuroptics Blueprint" needs to be "ash_prime_neuroptics" and not "ash_prime_neuroptics_blueprint"
    if ((('Prime' in name) and ('Neuroptics' in name)) or
    (('Prime' in name) and ('Chassis' in name)) or
    (('Prime' in name) and ('Systems' in name))):
        name = name.replace(' Blueprint', '')
    # lowercase the letters and replace spaces with underscores
    name = name.lower().replace(' ', '_')
    # replace ampersands with 'and' (silva & aegis)
    name = name.replace('&', 'and')
    return name

def get_orders(itemname):
    url_base = 'https://api.warframe.market/v1/items/'
    #...plus 'akbronco_prime_blueprint/orders?include=item'
    url_tail = '/orders?include=item'
    #formatted_itemname = itemname.lower().replace(' ', '_')
    formatted_itemname = format_item_name_for_market_url(itemname)
    url = url_base + formatted_itemname + url_tail
    print('url: ' + url)
    resp = requests.get(url)
    #market_page_dict = json.load(resp.content)
    market_page_dict = resp.json() # or json.loads(resp.text)
    print market_page_dict.keys()
    orders = market_page_dict['payload']['orders']
    return orders

def get_item_orders(itemname):
    raw_orders = get_orders(itemname)
    orders = get_online_sell_orders(raw_orders)
    #TODO: make sure the user's order is visible, and maybe check his region or platform?
    sorted_orders = sorted(orders, key=lambda price: price.get('platinum'))
    #for order in sorted_orders:
    #    print('%s: %s (quantity: %s)' % (order['user']['ingame_name'], order['platinum'], order['quantity']))
    return sorted_orders

def get_online_sell_orders(order_dict):
    os_orders = []
    for order in order_dict:
        #if order['order_type'] == 'sell' and order['user']['status'] == 'ingame':
        if valid_order(order):
            os_orders.append(order)
    return os_orders

def valid_order(order):
    # order is visible... maybe
    # order type is 'sell'
    if order['order_type'] != 'sell':
        return False
    # order is on platform 'pc'
    if order['platform'] != 'pc':
        return False
    # seller status is 'ingame'
    if order['user']['status'] != 'ingame':
        return False
    # seller is in region 'en' (for "english", I guess, the other ones seem to be 'fr' and 'ru')
    if order['user']['region'] != 'en':
        return False
    # you're good, I guess
    return True

#get the counts of all ducat prices
from collections import Counter
dpd = make_dpd(soup)
pricecounts = Counter()
for item, price in dpd.items():
    pricecounts[price] += 1

def find_ducat_candidate():
    candidate = None
    for item in fortyfives:
        orders = get_item_orders(item)
        #print('for item %s we have %s orders total' % (item, len(orders)))
        if len(orders) < 1:
            continue
        if orders[0]['platinum'] <= 3:
            lowest_three_sellers = []
            for i in range(min(3, len(orders))):
                # I want the three lowest selling users, but I don't want an IndexError if there's fewer than three sellers at all
                lowest_three_sellers.append(orders[i]['user']['ingame_name'])
            print('candidate item found: %s. lowest three sellers are: %s' % (item, lowest_three_sellers))
            print('warframe market URL: https://warframe.market/items/%s' % format_item_name_for_market_url(item))
            candidate = item
            break
    return candidate
"""
