import requests
import json

'''Utilizes cmc for token's market cap'''

def getMarketCaps(symbolList):

    #Passing list of symbols to receive market cap data to Coinmarketcap
    api_key = 'your API key'

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?CMC_PRO_API_KEY='
    url += api_key
    s = '&symbol=' + str(symbolList)
    url += s
    
    r = requests.get(url)
    rj = r.json()
    rDict = rj['data']

    #Create a list of market caps from token symbols collected
    capList = []
    symList = []

    for x in rDict:
        capList.append((rDict[x]['quote']['USD']['market_cap']))
        symList.append((rDict[x]['symbol']))

    symAndCaps = dict(zip(symList, capList))
        
    return symAndCaps