import requests
import json

#function calls token info api
def totleSymbols():
    r = requests.get('https://services.totlesystem.com/tokens')
    rj = r.json()
    rDict = rj['tokens']

    symbolList = []

    for d in rDict:
        symbolList.append(d['symbol'])
    #remove stablecoins from ETF
    symbolList.remove('DAI')


    return symbolList   

def TotlePrices():
    r = requests.get('https://services.totlesystem.com/tokens/prices')
    rj = r.json()
    rDict = rj['response']

    print (rDict)

def Exchanges():
    r = requests.get('https://services.totlesystem.com/exchanges')
    rj = r.json()

    print (rj)

def TotleSwap():

    address = '0x29126c4099c2d6e1dEBE2529CC5D983E5ed6fD7C'
    affiliate = '0xF8ca541e9dF7e314C86151c7Bd06449ae5B2094B'
    payload = {
        'address': '0x29126c4099c2d6e1dEBE2529CC5D983E5ed6fD7C',
        'affiliateContract' : '0xF8ca541e9dF7e314C86151c7Bd06449ae5B2094B', 
        'swap':{ 'from': '0x1985365e9f78359a9b6ad760e32412f4a445e862', 'to': '0xe41d2489571d322189246dafa5ebde1f4699f498', 'amount': 1000000000000000000}
    }
    r = requests.post('https://services.totlesystem.com/tokens', data=payload)



#prompt user for token 
#def findToken(x):
#    print ("What token do you wanna know about?")
#    x = input()
#    return x

#Exchanges()