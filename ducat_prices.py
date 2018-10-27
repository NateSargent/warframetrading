# ducat_prices.py
from bs4 import BeautifulSoup
import requests

# to rip ducat price information out of the wiki:
def get_ducat_prices_from_wiki():
    ducat_prices_url = 'http://warframe.wikia.com/wiki/Ducats/Prices/All'

    resp = requests.get(ducat_prices_url)
    html = resp.content
    soup = BeautifulSoup(html, 'html.parser')

    def make_dpd(soup):
        ducat_price_dict = {}
        for item in soup.find_all('tr')[1:]: # as of 10/25/2018, the 0th one isn't an item
            try:
                displayname = item.find_all('td')[0].find_all('a')[1].string
                ducatprice = item.find_all('td')[2].b.string
            except IndexError as ie:
                print('encountered IndexError for item %s' % displayname)
                continue
            ducat_price_dict[displayname] = ducatprice
        return ducat_price_dict
    return make_dpd(soup)

# to print this list:
#print('{')                                
#for key, value in dpd.items():            
#    print("   '%s': '%s'," % (key, value))
#print('}')

#notes:
"""
my ducat price dictionary ends up with 256 items. The wiki page (http://warframe.wikia.com/wiki/Ducats/Prices/All)
SAYS there are "186 rewards with 166 parts", but I think that's bullshit. I used ctrl-F on the page to count how often
each price appeared and got 256, the same amount as my dictionary, so I'm calling it good. I did this on 10/25/2018.
15 appeared on the page 97 times
25: 6 times
45: 78
65: 14
100: 61 (actually 62, but the first occurence on the page is the "1002" total rewards for all ducat items, it's not a price.)
"""

ducat_prices_dict = {
   'Akbolto Prime Blueprint': '15',
   'Akbolto Prime Barrel': '45',
   'Akbolto Prime Link': '45',
   'Akbolto Prime Receiver': '100',
   'Akbronco Prime Blueprint': '15',
   'Akbronco Prime Link': '45',
   'Aklex Prime Blueprint': '45',
   'Aklex Prime Link': '100',
   'Akstiletto Prime Blueprint': '100',
   'Akstiletto Prime Barrel': '45',
   'Akstiletto Prime Link': '45',
   'Akstiletto Prime Receiver': '45',
   'Ankyros Prime Blueprint': '15',
   'Ankyros Prime Blade': '65',
   'Ankyros Prime Gauntlet': '15',
   'Ash Prime Blueprint': '45',
   'Ash Prime Chassis Blueprint': '15',
   'Ash Prime Neuroptics Blueprint': '45',
   'Ash Prime Systems Blueprint': '65',
   'Ballistica Prime Blueprint': '100',
   'Ballistica Prime Lower Limb': '15',
   'Ballistica Prime Receiver': '45',
   'Ballistica Prime String': '45',
   'Ballistica Prime Upper Limb': '45',
   'Banshee Prime Blueprint': '45',
   'Banshee Prime Chassis Blueprint': '100',
   'Banshee Prime Neuroptics Blueprint': '15',
   'Banshee Prime Systems Blueprint': '100',
   'Bo Prime Blueprint': '15',
   'Bo Prime Handle': '45',
   'Bo Prime Ornament': '15',
   'Boar Prime Blueprint': '15',
   'Boar Prime Barrel': '45',
   'Boar Prime Receiver': '15',
   'Boar Prime Stock': '100',
   'Boltor Prime Blueprint': '100',
   'Boltor Prime Barrel': '15',
   'Boltor Prime Receiver': '45',
   'Boltor Prime Stock': '15',
   'Braton Prime Blueprint': '25',
   'Braton Prime Barrel': '15',
   'Braton Prime Receiver': '45',
   'Braton Prime Stock': '15',
   'Bronco Prime Blueprint': '15',
   'Bronco Prime Barrel': '45',
   'Bronco Prime Receiver': '15',
   'Burston Prime Blueprint': '15',
   'Burston Prime Barrel': '45',
   'Burston Prime Receiver': '15',
   'Burston Prime Stock': '15',
   'Carrier Prime Blueprint': '15',
   'Carrier Prime Carapace': '15',
   'Carrier Prime Cerebrum': '65',
   'Carrier Prime Systems': '15',
   'Cernos Prime Blueprint': '45',
   'Cernos Prime Grip': '15',
   'Cernos Prime Lower Limb': '100',
   'Cernos Prime String': '45',
   'Cernos Prime Upper Limb': '15',
   'Chroma Prime Blueprint': '15',
   'Chroma Prime Chassis Blueprint': '45',
   'Chroma Prime Neuroptics Blueprint': '100',
   'Chroma Prime Systems Blueprint': '100',
   'Dakra Prime Blueprint': '45',
   'Dakra Prime Blade': '65',
   'Dakra Prime Handle': '15',
   'Destreza Prime Blueprint': '45',
   'Destreza Prime Blade': '100',
   'Destreza Prime Handle': '15',
   'Dual Kamas Prime Blueprint': '15',
   'Dual Kamas Prime Blade': '100',
   'Dual Kamas Prime Handle': '45',
   'Ember Prime Blueprint': '100',
   'Ember Prime Chassis Blueprint': '15',
   'Ember Prime Neuroptics Blueprint': '15',
   'Ember Prime Systems Blueprint': '45',
   'Euphona Prime Blueprint': '15',
   'Euphona Prime Barrel': '45',
   'Euphona Prime Receiver': '100',
   'Fang Prime Blueprint': '15',
   'Fang Prime Blade': '15',
   'Fang Prime Handle': '25',
   'Fragor Prime Blueprint': '65',
   'Fragor Prime Handle': '65',
   'Fragor Prime Head': '15',
   'Frost Prime Blueprint': '100',
   'Frost Prime Chassis Blueprint': '15',
   'Frost Prime Neuroptics Blueprint': '15',
   'Frost Prime Systems Blueprint': '45',
   'Galatine Prime Blueprint': '100',
   'Galatine Prime Blade': '15',
   'Galatine Prime Handle': '45',
   'Glaive Prime Blueprint': '100',
   'Glaive Prime Blade': '45',
   'Glaive Prime Disc': '45',
   'Gram Prime Blueprint': '45',
   'Gram Prime Blade': '15',
   'Gram Prime Handle': '100',
   'Helios Prime Blueprint': '45',
   'Helios Prime Carapace': '15',
   'Helios Prime Cerebrum': '100',
   'Helios Prime Systems': '45',
   'Hikou Prime Blueprint': '15',
   'Hikou Prime Pouch': '15',
   'Hikou Prime Stars': '15',
   'Hydroid Prime Blueprint': '45',
   'Hydroid Prime Chassis Blueprint': '15',
   'Hydroid Prime Neuroptics Blueprint': '45',
   'Hydroid Prime Systems Blueprint': '100',
   'Kavasa Prime Band': '45',
   'Kavasa Prime Buckle': '65',
   'Kavasa Prime Collar Blueprint': '45',
   'Kogake Prime Blueprint': '45',
   'Kogake Prime Boot': '15',
   'Kogake Prime Gauntlet': '100',
   'Kronen Prime Blueprint': '15',
   'Kronen Prime Blade': '100',
   'Kronen Prime Handle': '45',
   'Latron Prime Blueprint': '15',
   'Latron Prime Barrel': '15',
   'Latron Prime Receiver': '15',
   'Latron Prime Stock': '15',
   'Lex Prime Blueprint': '25',
   'Lex Prime Barrel': '15',
   'Lex Prime Receiver': '15',
   'Limbo Prime Blueprint': '45',
   'Limbo Prime Chassis Blueprint': '100',
   'Limbo Prime Neuroptics Blueprint': '100',
   'Limbo Prime Systems Blueprint': '15',
   'Loki Prime Blueprint': '15',
   'Loki Prime Chassis Blueprint': '45',
   'Loki Prime Neuroptics Blueprint': '15',
   'Loki Prime Systems Blueprint': '100',
   'Mag Prime Blueprint': '100',
   'Mag Prime Chassis Blueprint': '45',
   'Mag Prime Neuroptics Blueprint': '15',
   'Mag Prime Systems Blueprint': '15',
   'Mirage Prime Blueprint': '100',
   'Mirage Prime Chassis Blueprint': '15',
   'Mirage Prime Neuroptics Blueprint': '15',
   'Mirage Prime Systems Blueprint': '45',
   'Nami Skyla Prime Blueprint': '15',
   'Nami Skyla Prime Blade': '100',
   'Nami Skyla Prime Handle': '45',
   'Nekros Prime Blueprint': '100',
   'Nekros Prime Chassis Blueprint': '15',
   'Nekros Prime Neuroptics Blueprint': '45',
   'Nekros Prime Systems Blueprint': '100',
   'Nikana Prime Blueprint': '65',
   'Nikana Prime Blade': '100',
   'Nikana Prime Hilt': '100',
   'Nova Prime Blueprint': '45',
   'Nova Prime Chassis Blueprint': '100',
   'Nova Prime Neuroptics Blueprint': '15',
   'Nova Prime Systems Blueprint': '15',
   'Nyx Prime Blueprint': '15',
   'Nyx Prime Chassis Blueprint': '65',
   'Nyx Prime Neuroptics Blueprint': '100',
   'Nyx Prime Systems Blueprint': '45',
   'Oberon Prime Blueprint': '45',
   'Oberon Prime Chassis Blueprint': '15',
   'Oberon Prime Neuroptics Blueprint': '100',
   'Oberon Prime Systems Blueprint': '100',
   'Odonata Prime Blueprint': '45',
   'Odonata Prime Harness Blueprint': '15',
   'Odonata Prime Systems Blueprint': '15',
   'Odonata Prime Wings Blueprint': '65',
   'Orthos Prime Blueprint': '45',
   'Orthos Prime Blade': '45',
   'Orthos Prime Handle': '15',
   'Paris Prime Blueprint': '15',
   'Paris Prime Grip': '45',
   'Paris Prime Lower Limb': '15',
   'Paris Prime String': '15',
   'Paris Prime Upper Limb': '25',
   'Pyrana Prime Blueprint': '100',
   'Pyrana Prime Barrel': '15',
   'Pyrana Prime Receiver': '45',
   'Reaper Prime Blueprint': '15',
   'Reaper Prime Blade': '45',
   'Reaper Prime Handle': '15',
   'Rhino Prime Blueprint': '100',
   'Rhino Prime Chassis Blueprint': '65',
   'Rhino Prime Neuroptics Blueprint': '45',
   'Rhino Prime Systems Blueprint': '15',
   'Rubico Prime Blueprint': '100',
   'Rubico Prime Barrel': '45',
   'Rubico Prime Receiver': '15',
   'Rubico Prime Stock': '45',
   'Saryn Prime Blueprint': '65',
   'Saryn Prime Chassis Blueprint': '100',
   'Saryn Prime Neuroptics Blueprint': '45',
   'Saryn Prime Systems Blueprint': '15',
   'Scindo Prime Blueprint': '45',
   'Scindo Prime Blade': '100',
   'Scindo Prime Handle': '45',
   'Sicarus Prime Blueprint': '15',
   'Sicarus Prime Barrel': '15',
   'Sicarus Prime Receiver': '100',
   'Silva & Aegis Prime Blueprint': '45',
   'Silva & Aegis Prime Blade': '45',
   'Silva & Aegis Prime Guard': '100',
   'Silva & Aegis Prime Hilt': '15',
   'Soma Prime Blueprint': '15',
   'Soma Prime Barrel': '15',
   'Soma Prime Receiver': '45',
   'Soma Prime Stock': '100',
   'Spira Prime Blueprint': '15',
   'Spira Prime Blade': '100',
   'Spira Prime Pouch': '100',
   'Sybaris Prime Blueprint': '15',
   'Sybaris Prime Barrel': '100',
   'Sybaris Prime Receiver': '45',
   'Sybaris Prime Stock': '15',
   'Tiberon Prime Blueprint': '45',
   'Tiberon Prime Barrel': '100',
   'Tiberon Prime Receiver': '15',
   'Tiberon Prime Stock': '100',
   'Tigris Prime Blueprint': '100',
   'Tigris Prime Barrel': '45',
   'Tigris Prime Receiver': '45',
   'Tigris Prime Stock': '15',
   'Trinity Prime Blueprint': '45',
   'Trinity Prime Chassis Blueprint': '45',
   'Trinity Prime Neuroptics Blueprint': '25',
   'Trinity Prime Systems Blueprint': '15',
   'Valkyr Prime Blueprint': '15',
   'Valkyr Prime Chassis Blueprint': '100',
   'Valkyr Prime Neuroptics Blueprint': '45',
   'Valkyr Prime Systems Blueprint': '100',
   'Vasto Prime Blueprint': '45',
   'Vasto Prime Barrel': '15',
   'Vasto Prime Receiver': '15',
   'Vauban Prime Blueprint': '100',
   'Vauban Prime Chassis Blueprint': '100',
   'Vauban Prime Neuroptics Blueprint': '100',
   'Vauban Prime Systems Blueprint': '100',
   'Vectis Prime Blueprint': '45',
   'Vectis Prime Barrel': '15',
   'Vectis Prime Receiver': '100',
   'Vectis Prime Stock': '65',
   'Venka Prime Blueprint': '45',
   'Venka Prime Blades': '15',
   'Venka Prime Gauntlet': '100',
   'Volt Prime Blueprint': '25',
   'Volt Prime Chassis Blueprint': '45',
   'Volt Prime Neuroptics Blueprint': '65',
   'Volt Prime Systems Blueprint': '45',
   'Wyrm Prime Blueprint': '15',
   'Wyrm Prime Carapace': '15',
   'Wyrm Prime Cerebrum': '15',
   'Wyrm Prime Systems': '45',
   'Zephyr Prime Blueprint': '100',
   'Zephyr Prime Chassis Blueprint': '45',
   'Zephyr Prime Neuroptics Blueprint': '15',
   'Zephyr Prime Systems Blueprint': '100',
}
