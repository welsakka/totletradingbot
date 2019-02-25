import json
from decimal import *
from totle import totleDecimals

def cPayload(cAddresses, ePercent, tPrice, walletAddress, dec):
    myPayload = dict(address=walletAddress, buys=[], sells=[])
    i = 0

    #Amount of tokens to be purchased per token
    tokenAmount = []
    while i < len(ePercent) :
        tokenAmount.append(ePercent[i]/tPrice[i])
        i += 1

    for x in tokenAmount:
        Decimal(x).quantize(Decimal('1000000000000000000.'), rounding=ROUND_DOWN)
    
    i = 0
    tempD = {}
    buysList = []
    while i < len(cAddresses):
        tempD = {'token': cAddresses[i], 'amount' : tokenAmount[i]}
        buysList.append(tempD)
        i += 1

    myPayload.update({'buys' : buysList})

    return myPayload


