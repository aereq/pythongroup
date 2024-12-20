# -*- coding: utf-8 -*-
"""mod.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zTxF3mqEVDJV0v0bKrqyHp98d6ZosIYe
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

"""# **function stock_return_risk()**"""

def stock_return_risk(ticker):
    data = yf.download(ticker, period="10y", interval="1d")
    if data.empty:
        raise ValueError(f"No data found for ticker {ticker}")
    data = data['Adj Close']
    daily_returns = data.pct_change().dropna()
    avg_daily_return = daily_returns.mean()
    daily_volatility = daily_returns.std()
    trading_days = 252  # Approximate number of trading days in a year
    avg_annual_return = (1 + avg_daily_return) ** trading_days - 1
    annual_volatility = daily_volatility * np.sqrt(trading_days)

    return avg_annual_return, annual_volatility

print(stock_return_risk("AAPL"))
#shows annual return (0,3) then annual volatility (0,28)

"""# function portfolio_return()"""

def portfolio_return(securities, weights):
    data = yf.download(securities, period="10y", interval="1d")['Adj Close']
    if data.empty:
        raise ValueError("No data found for the provided securities.")
    daily_returns = data.pct_change().dropna()
    avg_daily_returns = daily_returns.mean()
    trading_days = 252  # Approximate number of trading days in a year
    avg_annual_returns = (1 + avg_daily_returns) ** trading_days - 1
    portfolio_annual_return = np.dot(avg_annual_returns, weights)

    return portfolio_annual_return

print(portfolio_return(["AAPL", "MSFT"], np.array([0.6, 0.4])))

"""# function portfolio_risk()"""

def portfolio_risk(securities, weights):
    data = yf.download(securities, period="10y")['Adj Close']
    returns = data.pct_change().dropna()
    cov_matrix = returns.cov() * 252
    portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
    portfolio_volatility = np.sqrt(portfolio_variance)
    print(f"Annual portfolio risk/volatility: {portfolio_volatility:.4f}")

print(portfolio_risk(["AAPL", "MSFT"], np.array([0.6, 0.4])))