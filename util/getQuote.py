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

def testing(stockRawData):
    closing_prices = stockRawData.ix['Close']
    oneStock = closing_prices['QQQ']
    change = 100 * (oneStock[-1] - oneStock[0]) / oneStock[0]

    price_change = {}
    price_change['QQQ'] = change
    print(price_change)


    pc = pd.Series(price_change)
    pc.sort_values(inplace=True)
    #fig, ax = plt.subplots(figsize=(10,8))
    #pc.plot(kind='bar', ax=ax)

    #print(stockRawData.to_frame())

    sliceKey = 'Close'
    adjCloseData = stockRawData.ix[sliceKey]
    #print(adjCloseData)

    ibmAdjCloseData = adjCloseData['QQQ']
    #print(type(ibmAdjCloseData))
    #print(adjCloseData[2:5])
    #print(adjCloseData.pop('QQQ'))

if __name__ == "__main__":
    #nasdaq, nyse = importSymbols()
    tickers = ['QQQ','AAPL']
    numDays = 20

    start, end = startEndDatesToday(numDays)
    df1 = createDF(tickers, start, end)
    testing(df1)
