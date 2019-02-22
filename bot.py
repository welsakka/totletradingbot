
'''Welcome to ETF bot! You should provide API keys for getContractInfo.py, marketCap.py
and totle.py if needed. This bot is still a work in progress'''


import time, requests, json
from marketCap import getMarketCaps
from portfolioRebalance import calculateNewPortfolio, obtainTokenPercent, aggMarketCap
from getContractInfo import walletBalance
from totle import totleSymbols, TotleRebalance

#pull token symbols using Totle API. Uncomment to pull live data from Totle and CMC. WILL PULL ALL TOKENS, 
#NOT JUST TOP 20

#  symbolList = totleSymbols()
#  symbolList = [e for e in symbolList if e not in ('WETH_OLD', 'REP-OLD', 'DCL','DONUT','ENO','ENTRP','EQC','FLIP','WLK','XGM')]
#  s = ",".join(symbolList)
#  marketCapList = getMarketCaps(s)

#sample marketcaps of the top 20 pulled from Totle as of 5:45pm, 2/21/2019
#Add hashtags to the two lists below if you uncomment the lines above
marketCapList = [1657118263.00, 1472770946.00, 648012910.00, 182025458.00, 166002951.00, 156057596.00, 151483880.00, 151328735.00, 146127115.00, 114814488.00, 97968027.00, 86225302.00, 81910953.00, 81523240.00, 80927709.71, 72603818.00, 70640626.00, 68746234.00, 66295291.54, 63206322.00, 48665207.00]
symbolList = ['TRX','BNB','MKR','OMG','BAT','LINK','REP','ZIL','ZRX','NPXS','AE','BTM','PPP','THETA','SNT','PPT','R','PRL','GNT','MCO']

symbolsAndMarket = dict(zip(symbolList, marketCapList))
ethPercent = calculateNewPortfolio(list(symbolsAndMarket.values()))
percent = obtainTokenPercent(aggMarketCap(marketCapList),marketCapList)


print("The symbols to be added to the ETF are " + str(symbolList) + '\n')
print("The position percentage of each token is " + str(dict(zip(symbolList,percent))) + '\n')
print('The amount of Ether(wei) that must be spent for each token is ' + str(dict(zip(symbolList,ethPercent))) + '\n' )

print("Wallet Balance:" + walletBalance() + ' wei\n')


TotleRebalance()
