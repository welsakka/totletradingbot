from etherscan.accounts import Account
import json

#Use of Etherscan API to pull wallet balances
#Initialize function with your API key and address

def walletBalance(walletAddress):
    api_key = 'IVPR3T2CWJ2TKUYH6824HNGKKJ4ENEM9EU'

    api = Account(address=walletAddress, api_key=api_key)
    balance = api.get_balance()
    return balance