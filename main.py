
from blizzardapi import BlizzardApi
#from wowapi import WowApi
#import json
import requests
api_client = BlizzardApi("0f849df7ee2e4afd837b0762b8a86d9a", "ufpxBOICbmx4NvqKO0k9ehGV4uGDsP3R")
access_token = "US2Av9Yt8Z5j683XZPcSDkelNG0uHD46wH"
baseURL = "https://us.api.blizzard.com/"
region = "us"
locale = "en_US"



#enter a realm name to retrieve its id
realmName = input("Realm: ")
connectedRealmSearch = api_client.wow.game_data.get_realm(region, locale, realmName, is_classic=False)
realmId = connectedRealmSearch['id']

#enter the name of an item to retrieve it's id
itemName = input("Enter Item: ")
itemSearch = requests.get(baseURL + "data/wow/search/item?namespace=static-us&name.en_US=" + itemName + "&access_token=" + access_token)
itemSearch = itemSearch.json()
itemId = itemSearch['results'][0]['data']['id']

item = api_client.wow.game_data.get_item(region, locale, itemId, is_classic=False)

print(realmId)
print(itemId)
print(item)



auctions = api_client.wow.game_data.get_auctions(region, locale, realmId)


#print(realmId)
#print(itemName)
#print(itemId)
