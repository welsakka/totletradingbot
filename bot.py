import time, requests, json
import operator
import matplotlib
from marketCap import getMarketCaps
from portfolioRebalance import calculateNewPortfolio
from getContractInfo import walletBalance
from totle import totleSymbols


#pull token symbols using Totle API
symbolList = totleSymbols()
#symbolList = ['STU', 'ZIL', 'CBT', 'DNT', 'DATA', 'BAT', 'POE', 'MANA', 'AIX', 'BLT', 'QVT', 'SUB', 'GRID', 'CFI', 'NMR', 'CDT', 'UKG', 'RDN', 'AST', 'KICK', 'AIR', 'WAND', 'VEE', 'DENT', 'MBRS', 'THETA', 'WAX', 'RVT', 'SALT', 'FUN', 'CVC', 'SPANK', 'SNIP', 'AION', 'XAUR', 'FDX', 'HST', 'CAT', 'POWR', 'ETHOS', 'INS', 'AE', 'LOC', 'RLC', 'MWAT', 'CRED', 'ZAP', 'GNO', 'SNT', 'GBT', 'IFT', 'GOAL', 'CAG', 'LEND', 'NEWB', 'FYN', 'PTOY', 'AGI', 'REQ', 'REAL', 'ANT', 'SNM', 'POLY', 'QSP', 'MKR', 'JNT', 'INXT', 'FUCK', 'DOV', 'XRL', 'GMT', 'TKR', 'RPL', 'EVC', 'STORJ', 'HGT', 'ARN', 'MLN', 'WETH', 'TAU', 'STORM', 'OMG', 'BNTY', 'CND', 'PPT', 'PLU', 'LNK', 'ZRX', 'REP', 'UFR', 'TIX', 'FUEL', 'POW', 'EBTC', 'SHP', 'MTL', 'DGPT', 'GUP', 'RCN', 'ART', 'HDG', '1ST', 'ACE', 'ADST', 'ADT', 'ADX', 'AI', 'ALIS', 'AMB', 'AMM', 'ARCT', 'ASTRO', 'ATL', 'ATM', 'ATS', 'AVT', 'B2B', 'BAS', 'BBT', 'BET', 'BLN', 'BLUE', 'BLX', 'BMC', 'BNB', 'BNT', 'BON', 'BPT', 'BQ', 'BRAT', 'BTC2X', 'BTCM', 'BTCS', 'BTE', 'BTM', 'CASH', 'CCO', 'CCT', 'CL', 'CLD', 'CMT', 'COB', 'COSS', 'CREDO', 'CRTM', 'CSNO', 'CTR', 'CTX', 'DALC', 'DAY', 'DBET', 'DCN', 'DICE', 'DIVX', 'DLT', 'DNA', 'DRGN', 'DRP', 'DRPU', 'DRT', 'EAGLE', 'EBCH', 'EBET', 'EBIT', 'ECASH', 'EDG', 'EDO', 'EGAS', 'EGOLD', 'ELITE', 'ELIX', 'ENG', 'ENJ', 'EOS', 'EPY', 'ERC20', 'EREAL', 'ERO', 'ETBS', 'ETG', 'EUSD', 'EVX', 'EXN', 'EXRN', 'FAP', 'FC', 'FLIK', 'FLIXX', 'FRD', 'FYP', 'GIM', 'GOOD', 'GVT', 'HAT', 'HBT', 'HMQ', 'HVN', 'HYTV', 'IBTC', 'ICE', 'ICN', 'ICOS', 'IETH', 'IND', 'INDI', 'IQT', 'IXT', 'JET', 'KEY', 'KIN', 'KNC', 'LA', 'LCT', 'LEV', 'LIFE', 'LINK', 'LLT', 'LTG', 'LUN', 'MCAP', 'MCI', 'MCO', 'MGO', 'MOD', 'MSP', 'MTH', 'MTX', 'MVC', 'MYST', 'NDC', 'NET', 'NEU', 'NIMFA', 'NTC', 'NTWK', 'NULS', 'NXC', 'OAX', 'ONG', 'OPT', 'ORME', 'PAY', 'PAYX', 'PBL', 'PFR', 'PGL', 'PKT', 'PLBT', 'PLC', 'PLR', 'POLL', 'POS', 'PPP', 'PRG', 'PRIX', 'PRL', 'PRO', 'PST', 'QAU', 'R', 'READ', 'REX', 'RIYA', 'SCL', 'SDRN', 'SGR', 'SKIN', 'SMART', 'SMT', 'SNC', 'SND', 'SNGLS', 'SNOV', 'SOAR', 'SSS', 'STAR', 'STRC', 'STX', 'SWFTC', 'SWM', 'SWP', 'SWT', 'TAAS', 'TFL', 'TGT', 'TIE', 'TIME', 'TKN', 'TNT', 'TRST', 'TRX', 'UGT', 'VEN', 'VERI', 'VIB', 'VIBE', 'VIU', 'VOISE', 'WABI', 'WIC', 'WILD', 'WINGS', 'WISH', 'WRC', 'WTC', 'XMRG', 'XNN', 'XPA', 'XUC', 'ZCG', 'ZSC', 'RHOC', 'NXX', 'SXDT', 'NPXS', 'DGX', 'ELEC', 'ATMI', 'SCT', 'GNT', 'LRC', 'XDCE', 'NEXO', 'ROCK2',]

#CODE FOR PULLING MARKETCAP DATA FROM CMC API; NEEDS WORK, SO HARDCODED VALUES IN THE MEANTIME
#########################################################################
#  s = ",".join(symbolList)
#  use list of token symbols to pull market cap data from CoinMarketCap
#  marketCapList = getMarketCaps(s)
#  Sort market caps from highest to lowest, and take only the top 20
#  symbolsAndMarketCaps = dict(zip(symbolList, marketCapList))
#  sorted_d = sorted(symbolsAndMarketCaps.items(), key=operator.itemgetter(1))
#  marketCapList.sort(reverse = True)
#  marketCapList[:21]
############################################################################

#sample marketcaps of the top 20 pulled from Totle as of 5:45pm, 2/21/2019
marketCapList = [1657118263.00, 1472770946.00, 648012910.00, 182025458.00, 166002951.00, 156057596.00, 151483880.00, 151328735.00, 146127115.00, 114814488.00, 97968027.00, 86225302.00, 81910953.00, 81523240.00, 80927709.71, 72603818.00, 70640626.00, 68746234.00, 66295291.54, 63206322.00, 48665207.00]
symbolList = ['TRX','BNB','MKR','OMG','BAT','LINK','REP','ZIL','ZRX','NPXS','AE','BTM','PPP','THETA','SNT','PPT','R','PRL','GNT','MCO']

print("wallet balance:", walletBalance())
percent = calculateNewPortfolio(marketCapList)

symbolsAndPercent = dict(zip(symbolList, percent))
print (symbolsAndPercent)



