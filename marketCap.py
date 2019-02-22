import requests
import json
from collections import defaultdict

'''Utilizes cmc for token's market cap'''

def getMarketCaps(symbolList):

    #Passing list of symbols to receive market cap data to Coinmarketcap
    #api_key = '480d8ae5-0b95-4df7-8b98-ac918551111e'
   # concatenate = '?CMC_PRO_API_KEY=' + api_key
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?CMC_PRO_API_KEY=480d8ae5-0b95-4df7-8b98-ac918551111e&symbol=' + str(symbolList)
    #'?symbol=' + symbolList
    r = requests.get(url)
    rj = r.json()
    rDict = rj['data']
    
    #Create a list of market caps from token symbols collected
    marketCapList = []
    x = 0
    while x < 20:
        marketCapList.append(rj['data']['id'])
        x += 1

    return marketCapList