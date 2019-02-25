
'''Welcome to ETF bot! You should provide API keys for getContractInfo.py, marketCap.py
and totle.py if needed. This bot is still a work in progress'''


import time, requests, json, string
from marketCap import getMarketCaps
from portfolioRebalance import calculateNewPortfolio, obtainTokenPercent, aggMarketCap
from getWallet import walletBalance
from totle import totleAddresses, totleRebalance, totleBids
from constructPayload import cPayload

#Input the symbols you are interested in including in the ETF, and the wallet you want to interact with

symbolList = ['TRX','BNB','MKR','OMG','BAT','LINK','REP','ZIL','ZRX','NPXS','AE','BTM','PPP','THETA','SNT','PPT','R','MCO']
wallet = "0x29126c4099c2d6e1dEBE2529CC5D983E5ed6fD7C"

s = ",".join(symbolList)

#Pull market caps from CoinMarketCap API
####   UNCOMMENT THE LINE BELOW TO PULL THE LATEST VALUES FOR MARKET CAPS ####
#symsAndCaps = getMarketCaps(s)

#sample marketcaps of the above symbols as of 5:28 PM, 2/23/2019
#All marketcaps are zipped together with their respective tokens into dictionaries
#### DELETE LINE BELOW IF YOU WISH TO HAVE LATEST MARKET CAP DATA ####
symsAndCaps = {'AE': 110616028.7491738, 'BAT': 176180236.0371023, 'BNB': 1528138527.5502732, 'BTM': 107908389.37092498, 'LINK': 161257248.3207, 'MCO': 47891331.91474555, 'MKR': 736260770.2210001, 'NPXS': 121042231.38820533, 'OMG': 188407893.63948122, 'PPP': 10321151.851725, 'PPT': 70256074.5472155, 'R': 68278133.57607299, 'REP': 156271009.3395, 'SNT': 78876592.15510762, 'THETA': 86962303.3296093, 'TRX': 1695425046.3470254, 'ZIL': 161465729.23760486, 'ZRX': 150122797.95562127}

#Pull token addressses and bids
symbolContractAddresses = totleAddresses(symbolList)
symbolBids = totleBids(symbolContractAddresses)
ethPercent = calculateNewPortfolio(list(symsAndCaps.values()), wallet)
payload = cPayload(symbolContractAddresses, ethPercent, symbolBids, wallet)

percent = obtainTokenPercent(aggMarketCap(list(symsAndCaps.values())), list(symsAndCaps.values()))

newSymbols = list(symsAndCaps.keys())
print("The symbols to be added to the ETF are " + str(newSymbols) + '\n')
print("The position percentage of each token is " + str(dict(zip(newSymbols,percent))) + '\n')
print('The amount of Ether(wei) that must be spent for each token is ' + str(dict(zip(newSymbols,ethPercent))) + '\n' )

print("Wallet Balance:" + walletBalance(wallet) + ' wei\n')
