#!/usr/bin/env python
# Make sure to first run:
# source activate finance

# Company info can be downloaded here: http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download
# and here: http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download

import pandas_datareader.data as web
qqq = web.get_quote_yahoo('QQQ')
print(qqq)
print(type(qqq))

def getQuote(symbolList):
    quoteList = []
    for stock in symbolList:
        x = web.get_quote_yahoo(stock)
        quoteList.append(x)

    return quoteList

# import symbol lists
from symbols import getSymbolLists
nasdaq = getSymbolLists('NASDAQ')
print(len(nasdaq))

nyse = getSymbolLists('NYSE')
print(len(nyse))

def getPrice():
    import pandas
    #import pandas.io.data as web
    #from datetime import datetime
    import datetime

    tickers = ['QQQ']
    start = datetime.datetime(2014,1,1)
    #end = datetime.datetime(2014,1,3)
    start = datetime.date.today() - datetime.timedelta (4)
    end = datetime.date.today()
    stockRawData = web.DataReader(tickers, 'yahoo', start, end)
    print(stockRawData.to_frame())

    sliceKey = 'Adj Close'
    sliceKey = 'Low'
    adjCloseData = stockRawData.ix[sliceKey]
    print(adjCloseData)

    ibmAdjCloseData = adjCloseData['QQQ']
    print(ibmAdjCloseData)

getPrice()
