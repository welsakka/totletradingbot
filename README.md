# Totle ETF bot

This bot is purposed to pull data from various API's from Totle and other third-party sources to create
a diversified wallet of ERC20 tokens listed on Totle's exchange. Tokens are ranked according to market cap,
and the ETF's positions per token will be based on:

*Token's market cap / Aggregated market cap*

The chosen wallet makes a POST request to Totle's exchange for purchasing tokens. Rebalancing the wallet can be achieved by
liquidating the entire account at the end of some time period, or by utilizing Totle's swap endpoint. 

All code is written in python, and imports various libraries for help. To start the bot, run Bot.py

### How could this project be targeted at consumers/businesses?
ETF's are known to be a reliable way for any investor/institution to gain exposure in a selected market. As opposed to 
actively traded funds, ETF's are 'passive', and diversify their positions in many entities in one market. This
makes ETF's competitive compared to other funds, as they minimize risk well, and capture the general move of a market.
Various financial vehicles have already been created for the most popular Cryptocurrencies, including private
investment funds, mutual funds, and even ETF's. Ethereum is one of the most popular platforms in the market today, and much of 
the mainstream audience have heard of tokens, ICO's and airdrops, especially during 2017, when they were covered by major
news networks and gained popularity.
However, the obstacles to participate in these opportunities are still too great, despite developers' best efforts to make
cryptos user-friendly. This includes the steep learning-curve of blockchain, understanding the Ethereum ecosystem, and more.
Therefore, I propose that allowing users to particpate in an ETF will: 
1. Ease new users into the ecosystem of tokens 
2. Increase participation in various platforms 
3. Allow large institutions to gain exposure to the token market in a cheap and convinient way.
4. Create arbitrage opportunities for traders and Authorized Participants (or automatic burning/distribution of tokens)
Totle's API and platform are the perfect match for a Token ETF, simply because they are able to aggregate prices from various DEX's,
making the most fair and accurate order book for any token.

A rough draft idea on how to implement an ETF is to create a multi-signiture wallet that has access to the Totle exchange. An ERC-20 or security token could be created to represent shares in the ETF, using oracles to get constant price updates on the ETF.

### Additional ways to expand on this idea
1. Create an index of tokens to benchmark the performance of the ETF
3. Remove use of third-party API's and soley use Totle API's
