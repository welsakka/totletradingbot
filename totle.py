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

#This function pulls bids for the selected tokens using Totle's API
#A price is calculated by averaging all the bids available
#for one token
def totleBids(add):
    r = requests.get('https://services.totlesystem.com/tokens/prices')
    rj = r.json()
    rDict = rj['response']

    addressList = {}
    
    #Get values in response for the contract addresses we are interested in
    for x in add:
        if(x in add and list(rDict.keys())):
            addressList.update({x: rDict[x]})

    #Get bid values for each contract address
    bidList = []
    for x in addressList:
        bidList.append(addressList[x])

    #Where i is a counter variable, temp holds bid values for a single contract address,
    #tempAvg holds a single bid price, and realAvg is our return value
    i = 0
    temp = []
    tempAvg = 0
    realAvg = []

    while i < (len(bidList)):
        float_avg = 0
        counter = 0
        temp = (bidList[i])
        
        for x in temp:
            tempAvg = temp[x]['bid']
            if(tempAvg == None): break
            float_avg += float(tempAvg)
            counter += 1
            
        #Average bid for a single token
        float_avg = float_avg / counter
        realAvg.append(float_avg)
        i = i + 1
        
    return realAvg 

def totleRebalance(payload):
    r = requests.post('https://services.totlesystem.com/rebalance', data=payload)
    print(r.text)