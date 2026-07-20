import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

def download_yfinance(ticker : str, start_date : datetime, end_date : datetime, interval : str = '1d'):
    data = yf.download(ticker, start_date, end_date, interval)
    return data

def ema(history, time):
    history[f'EMA_{time}'] = history['Close'].ewm(span=time, adjust=False).mean()
    return history

def sma(data, period):
    df = data.copy()
    df[f"SMA_{period}"] = df['Close'].rolling(period).mean()
    return df

def backtest (data, long_period, short_period, average_type):
    data = average_type(data, short_period)
    data = average_type(data, long_period)
    funcname = average_type.__name__.upper()
    data = data.assign(
        lagged_short = data[f'{funcname}_{short_period}'].shift(1),
        lagged_long = data[f'{funcname}_{long_period}'].shift(1),
        )
    data["signal"] = np.select(
            [
                (data[f'{funcname}_{short_period}'] >= data[f'{funcname}_{long_period}']) & (data["lagged_short"] <= data["lagged_long"]),
                (data[f'{funcname}_{short_period}'] <= data[f'{funcname}_{long_period}']) & (data["lagged_short"] >= data["lagged_long"])
            ],
    ["Buy", "Sell"],
    default= None)
    return data

def profit_and_loss(data):
    data = data[data["signal"].notnull()]
    data = data.loc[:, ["Close", "signal"]]
    buy_price = None
    transactions = []
    for price, signal in data.itertuples(index=False, name=None):
        if signal == "Buy":
            buy_price = price
        elif signal == "Sell" and buy_price is not None:
            transactions.append(price - buy_price)
            buy_price = None
    return f"P&L: {sum(transactions):.2f} USD \ntransactions: {transactions}"

def plot_graph(data, long_period, short_period, average_type):
    funcname = average_type.__name__.upper()
    plt.figure(figsize = (12, 10))
    plt.plot(data.index, data["Close"], label="price", color="blue")
    plt.plot(data.index, data[f"{funcname}_{short_period}"], label=f"{short_period}days_period_moving_average", color="orange")
    plt.plot(data.index, data[f"{funcname}_{long_period}"], label=f"{long_period}days_period_moving_average", color="purple")
    buy = data[data["signal"]=="Buy"]
    sell = data[data["signal"]=="Sell"]
    plt.scatter(buy.index, buy["Close"], label="Buy", color="green")
    plt.scatter(sell.index, sell["Close"], label="Sell", color="red")
    plt.title(f"Price, {funcname}_{short_period} and {funcname}_{long_period}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

data = download_yfinance("ETH-USD", start_date=datetime(2025,7,15), end_date=datetime(2026,7,15))
data = backtest(data, 50,20,sma)
profit = profit_and_loss(data)
print(profit)
plot_graph(data, 50, 20, sma)
