import requests
import json

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

def TotleRebalance():
    payload = {
        'address': '0x29126c4099c2d6e1dEBE2529CC5D983E5ed6fD7C',
        'buys' : [ 
            {
                'token' : '0x107c4504cd79c5d2696ea0030a8dd4e92601b82e',
                'amount' : '100000000000000000'
            }
            ]
    }
    r = requests.post('https://services.totlesystem.com/tokens', data=payload)
    print(r.text)

    #requires authentication?
