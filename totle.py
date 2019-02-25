import requests
import json

def totleAddresses(sym):
    r = requests.get('https://services.totlesystem.com/tokens')
    rj = r.json()
    rDict = rj['tokens']

    addressList = []

    for x in sym:
        for i in rDict:
            if i['symbol'] == x:
                addressList.append(i['address'])

    return addressList 

def totleBids(add):
    r = requests.get('https://services.totlesystem.com/tokens/prices')
    rj = r.json()
    rDict = rj['response']

    addressList = {}

    for x in add:
        for i in rDict:
            if i == x:
                addressList[x] = rDict[i]

    bidList = []
    for x in addressList:
        bidList.append(addressList[x])
    
    i = 0
    test = []
    avgBidList = []
    realAvg = []

    while i < (len(add) - 1):
        float_avg = 0
        counter = 0
        test = (bidList[i])
        
        for x in test:
            avgBidList = test[x]['bid']
            float_avg += float(avgBidList)
            counter += 1
            

        float_avg = float_avg / counter
        realAvg.append(float_avg)
        i += 1
 
    return avgBidList 


def totleRebalance():
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
