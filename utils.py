import pandas as pd
import yfinance as yf

def load_data(ticker="AAPL"):
    data = yf.download(ticker, start="2015-01-01", end="2025-01-01")
    data = data[['Close']]
    data['Prev_Close'] = data['Close'].shift(1)
    data = data.dropna()
    return data
