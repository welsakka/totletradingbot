
'''Welcome to ETF bot! You should provide API keys for getContractInfo.py, marketCap.py
and totle.py if needed. This bot is still a work in progress'''


import time, requests, json, sys, math
from constructPayload import cPayload
from marketCap import getMarketCaps
from portfolioRebalance import calculateNewPortfolio, obtainTokenPercent, aggMarketCap
from getWallet import walletBalance
from totle import *

#Input the symbols you are interested in including in the ETF, and the wallet you want to interact with

symbolList = ['TRX','BNB','MKR','OMG','BAT','LINK','REP','ZIL','ZRX','NPXS','AE','BTM','PPP','THETA','SNT','PPT','R','MCO']
wallet = input("Paste your wallet address here: ")

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
symDecimals = totleDecimals(symbolList)
payload = cPayload(symbolContractAddresses, ethPercent, symbolBids, wallet, symDecimals)

percent = obtainTokenPercent(aggMarketCap(list(symsAndCaps.values())), list(symsAndCaps.values()))

newSymbols = list(symsAndCaps.keys())
print("Wallet Balance: " , float(walletBalance(wallet)) / math.pow(10,18) ,'ETH\n')
print("The symbols to be added to the ETF are " + json.dumps(newSymbols,sort_keys=True,indent=4) + '\n')
print("The position percentage of each token is " + json.dumps(dict(zip(newSymbols,percent)),sort_keys=True, indent=4) + '\n')
print('The amount of Ether that must be spent for each token is ' 
+ json.dumps(dict(zip(newSymbols,ethPercent)), sort_keys=True, indent=4) + '\n' )

confirm = input("Would you like to diversify your wallet into these tokens(Y/N)?")
if confirm == "y":
    totleRebalance(payload)
elif confirm == "n":
    print ('Bot shutting down')
    sys.exit()
else:
    print ('Invalid response')
