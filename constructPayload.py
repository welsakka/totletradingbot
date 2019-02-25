
def cPayload(cAddresses, ePercent, tPrice, walletAddress):
    myPayload = dict(address=walletAddress, buys=[])
    i = 0

    #Amount of tokens to be purchased per token
    tokenAmount = []
    while i < len(ePercent) :
        tokenAmount.append(ePercent[i]/tPrice[i])
        i += 1
    i = 0

    tempD = {}
    buysList = []
    while i < len(cAddresses):
        tempD = {'token': cAddresses[i], 'amount' : tokenAmount[i]}
        buysList.append(tempD)
        i += 1

    myPayload.update({'buys' : buysList})

    return myPayload


