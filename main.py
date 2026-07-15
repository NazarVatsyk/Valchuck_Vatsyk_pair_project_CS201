import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
start_date = datetime(2025,7,15)
end_date = datetime(2026,7,15)
df_eth = yf.download('ETH-USD', start_date, end_date, interval='1d')

def sma(data, period):
    df = data.copy()
    df[f"SMA_{period}"] = df['Close'].rolling(period).mean()
    return df



