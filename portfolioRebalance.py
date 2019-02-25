from getWallet import walletBalance

#return dictionary of token symbols to ETH values in wei

#### WALLET MUST BE FUNDED WITH ONLY ETH TO ENSURE ALL FUNDS ####
####             ARE DISTRIBUTED PROPERLY                    ####
def calculateNewPortfolio(marketCapList):
    D = aggMarketCap(marketCapList)
    P = obtainTokenPercent(D, marketCapList)
    Y = obtainEthPercent(walletBalance(), P)

    #Returns a list of how much of each token should be held in 
    #a wallet of ETH. List positions correspond to the symbolsList in bot.py
    return Y


#aggregate market cap of tokens
def aggMarketCap(marketCapList):
    x = 0
    for i in marketCapList:
        x += i
    
    return x

#where x is aggregate market cap, marketCapList is a list of the token
#market caps, with respect to the symbolsList in bots.py
def obtainTokenPercent(x, marketCapList):

    tokenPercent = []
    for i in marketCapList:
        tokenPercent.append(i/x)

    return tokenPercent


#Takes amount of ETH in a wallet, and multiplies it by each element
#in the tokenPercent list
def obtainEthPercent(wB, tokenPercent):
    ethPercent = []

    for i in tokenPercent:
        ethPercent.append(i * int(wB))

    return ethPercent