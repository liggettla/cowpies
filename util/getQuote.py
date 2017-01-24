#!/usr/bin/env python
# Make sure to first run:
# source activate finance

# Company info can be downloaded here: http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download
# and here: http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download

# Find materials here: http://lectures.quantecon.org/py/index.html

import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
from datetime import timedelta
from datetime import date

# Get lists of all nyse/nasday tickers over mrkt cap of 1bln
def importSymbols():
    from symbols import getSymbolLists
    nasdaq = getSymbolLists('NASDAQ')
    nyse = getSymbolLists('NYSE')
    return nasdaq, nyse

def getQuote(symbol):
    quote = web.get_quote_yahoo(symbol)
    return quote

# Give specified start and end dates
def startEndDates():
    start = dt(2014,1,1)
    end = dt(2014,1,20)
    return start, end

# Give start and end dates by number of days before today
def startEndDatesToday(numDays):
    start = date.today() - timedelta(numDays)
    end = date.today()
    return start, end

def createDF(tickers, start, end):
    stockRawData = web.DataReader(tickers, 'yahoo', start, end)
    return stockRawData

# Give total change in stock price of period of time
def getTotalReturn(symbol, df):
    closing_prices = df.ix['Close']
    oneStock = closing_prices[symbol]
    change = 100 * (oneStock[-1] - oneStock[0]) / oneStock[0]
    price_change = {}
    price_change[symbol] = change
    return change

def plotClose(df):
    ax = df['Close'].plot(title='Closing Prices', fontsize=12)
    ax.set_xlabel('Time')
    ax.set_ylabel('Close')
    plt.show()

    ax = df['Adj Close'].plot(title='Adjusted Closing Prices', fontsize=12)
    ax.set_xlabel('Time')
    ax.set_ylabel('Adj Close')
    plt.show()

def plotVolume(df):
    ax = df['Volume'].plot(title='Volume', fontsize=12, kind='bar')
    ax.set_xlabel('Time')
    ax.set_ylabel('Volume')
    plt.show()

# This is not yet functional, refer to 6_histograms for help
def compute_daily_returns(df):
    daily_returns = df.copy() # copy the dataFrame so that values can be altered
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1 # compute for row 1 onwards
    daily_returns.ix[0, :] = 0 # set daily returns for row 0 to 0
    #daily_returns = (df /df.shift(1)) - 1
    #daily_returns.ix[0, :] = 0
    return daily_returns

# Computes global stats on all data in range
def globalStats(df):
    print('Mean: ')
    print(df.mean())
    print('\nMedian: ')
    print(df.median())
    print('\nStdDev: ')
    print(df.std())

# Plot stock prices
def plotData(df, slicekey, title='Stock Prices', xlabel='Date', ylabel='Price'):
    # ax here is a plot object
    # slice key is Close, Adj Close, Volume etc
    ax = df[slicekey].plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()

def testing(stockRawData):
    pass

if __name__ == "__main__":
    nasdaq, nyse = importSymbols()
    tickers = ['QQQ','AAPL']
    numDays = 180

    start, end = startEndDatesToday(numDays)
    df1 = createDF(tickers, start, end)


    testing(df1)
