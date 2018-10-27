#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
#from bs4 import BeautifulSoup
#from beautifulsoup4 import BeautifulSoup
#import subprocess
#from ducat_prices import ducat_prices_dict

from wfplattoduc import get_valid_orders, format_item_name_for_market_url

marketbaseurl = 'https://api.warframe.market/v1/items/'
markettailurl = '/orders?include=item'

sculptures = {
    'anasa ayatan sculpture': {'endo': 3450, 'slots': 4},
    'orta ayatan sculpture': {'endo': 2700, 'slots': 4},
    'vaya ayatan sculpture': {'endo': 1800, 'slots': 3},
    'piv ayatan sculpture': {'endo': 1725, 'slots': 3},
    'valana ayatan sculpture': {'endo': 1575, 'slots': 3},
    'sah ayatan sculpture': {'endo': 1500, 'slots': 3},
    'ayr ayatan sculpture': {'endo': 1425, 'slots': 3}
    }

"""
def get_valid_orders(itemname):
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
"""

for item, data in sculptures.items():
    print('%s:' % item)
    endo = data['endo']
    max_slots = data['slots']
    orders = get_valid_orders(item)
    orders = sorted(orders, key=lambda price: price.get('platinum'))
    # let's take the cheapest 3 orders
    orders = orders[:3]
    #print len(orders)
    if len(orders) < 1:
        continue
    for order in orders:
        result_dict = {}
        result_dict['item'] = item
        result_dict['seller'] = order['user']['ingame_name']
        result_dict['price'] = order['platinum']
        result_dict['quantity'] = order['quantity']
        ratio = endo/int(order['platinum'])
        result_dict['ratio'] = ratio
        slotted = order['mod_rank']
        if slotted == max_slots:
            slottedmsg = 'fully slotted'
        else:
            slottedmsg = '%s/%s slots' % (slotted, max_slots)
        print('%s selling %s %s at %sp, %s, endo-per-plat ratio: %s' % (order['user']['ingame_name'], order['quantity'], item, order['platinum'], slottedmsg, ratio))
        print('chatmessage:\n/w %s WTB %s at %sp' % (order['user']['ingame_name'], item, order['platinum']))
        #print('warframe market URL: https://warframe.market/items/%s' % format_item_name_for_market_url(item))
        #result_dict['market_url'] = 'https://warframe.market/items/%s' % item
        #chatmessage = '/w %s WTB %s at %sp, I\'ll take more than one' % (order['user']['ingame_name'], item, order['platinum'])
        #result_dict['chatmessage'] = '/w %s WTB %s at %sp, I\'ll take more than one' % (order['user']['ingame_name'], item, order['platinum'])
        #subprocess.call('echo %s | clip' % chatmessage, shell=True)
        #return result_dict
    print('\n')
