from main import *
import pandas as pd
import numpy as np
import json

def generator (start_price, duration, variance):
    rng = np.random.default_rng()
    samples = rng.normal(loc=0, scale=variance, size=duration)
    df = {'Close': samples}
    df = pd.DataFrame(df)
    df["Close"] = df["Close"].cumsum()
    df["Close"] = df["Close"] + start_price
    return df

# prices = generator(100,100,10)
# print(backtest(prices, 50, 20, sma))

parameters = [(21,9,sma, 100),(21,9,sma, 365), (21,9,sma,1000),
              (21,9,ema, 100),(21,9,ema, 365), (21,9,ema,1000),
              (50,20,sma, 100),(50,20,sma, 365), (50,20,sma,1000),
              (50,20,ema, 100),(50,20,ema, 365), (50,20,ema,1000),
              (100,50,ema, 365),(100,50,ema,1000),(100,50,sma, 365),
              (100,50,sma,1000),(200,100,sma, 365), (200,100,sma,1000),
              (200,100,ema, 365),(200,100,ema,1000)]
res = {}
for x in parameters:
    dummy = []
    for i in range(1000):
        df = generator(1, x[3], 0.05)
        df = backtest(df, x[0], x[1], x[2])
        dummy.append(float(profit_and_loss(df).split()[1]))
    res[x]={"mean": float(np.mean(dummy)), "var": float(np.var(dummy))}
print(res)
print(sorted(res.items(), key=lambda x: x[1]["mean"])[-1])
print(pd.DataFrame(res).T)