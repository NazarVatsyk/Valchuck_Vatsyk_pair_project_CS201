import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
start_date = datetime(2025,7,15)
end_date = datetime(2026,7,15)
df_eth = yf.download('ETH-USD', start_date, end_date, interval='1d')

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
final = backtest(df_eth, 200,50,sma)
print(final)
print(final[final["signal"].notnull()])
