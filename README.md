# Valchuck_Vatsyk_pair_project_CS201
Moving crossover strategies on Ethereum
##1. The instrument
Ticker: ETH-USD (Ethereum priced in US dollars).
What it is: the token of Ethereum, a blockchain platform that runs
smart contracts.
Data source: daily price history (open/high/low/close/volume) from
Yahoo Finance.

##2. Rationale
Ethereum is the #2 cryptocurrency by market cap, with billions of 
dollars traded every day. High trading volume means the price is set
by many independent participants, which is better for identifying trends.

A moving average crossover strategy only works if the price has stretches
where it moves consistently in one direction, rather than bouncing around
randomly. ETH is a good candidate because, over the last two years, it 
has gone through clear, sustained moves. It is also volatile enough for 
the algorithm to produce meaningful signals, and to produce them frequently.

##3. Tools
We have used python libraries such as Pandas, Numpy, Matplotlib, and yfinance. 
Yfinance was used to get the desired data, Pandas was used to manipulate 
the data conveniently, and Matplotlib to make visualisations. Numpy was used 
to run monte carlo siimulation to find out which strategy is the best for 
assets with different volatility

##4. Results
The backtest showed that our strategy would not have been appropriate for the last
year, since the P&L is lower then 0. Yet the graph also shows that the last year 
wasn't successful for crypto sharks. It is worth to mention that 21/9 EMA
crossover is widely used among cryptoinvestors. This strategy would have yielded
positive P&L for last two years.
