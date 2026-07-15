# Valchuck_Vatsyk_pair_project_CS201
Moving crossover strategies on Ethereum
1. The instrument
Ticker: ETH-USD (Ethereum priced in US dollars).
What it is: the token of Ethereum, a blockchain platform that runs
smart contracts.
Data source: daily price history (open/high/low/close/volume) from
Yahoo Finance.
2. Rationale
Ethereum is the #2 cryptocurrency by market cap, with billions of dollars
traded every day. High trading volume means the price is set by many
independent participants, which is better for seeking trends.
A moving average crossover strategy only works if the price has stretches
where it moves consistently in one direction, rather than
bouncing randomly. ETH is a good candidate because over the last two years
it has gone through clear, sustained moves. It is also actually volatile enough
for algorithm to produce meaningfull signals and to produce them freaquently
3.Tools
We have used python libraries such as Pandas, Numpy, and yfinance
