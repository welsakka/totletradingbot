from etherscan.accounts import Account
import json

#Use of Etherscan API to pull wallet balances
#Initialize function with your API key and address

def walletBalance():
    api_key = 'IVPR3T2CWJ2TKUYH6824HNGKKJ4ENEM9EU'
    address = '0x29126c4099c2d6e1dEBE2529CC5D983E5ed6fD7C'

    api = Account(address=address, api_key=api_key)
    balance = api.get_balance()
    return balance