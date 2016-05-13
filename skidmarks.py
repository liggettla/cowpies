#!/usr/bin/python

#https://pypi.python.org/pypi/yahoo-finance
#https://pypi.python.org/pypi/googlefinance

from googlefinance import getQuotes
from yahoo_finance import Share
from yahoo_finance import Currency

################
#Check For Data#
################
from os.path import isdir
from os import makedirs
if isdir('./userData'):
    pass
else:
    makedirs('./userData')


#Info
securList =  ['AAPL', 'XLV']
quotes = getQuotes(securList)
for i in quotes:
    index = i['Index']
    symbol = i['StockSymbol']
    price = float(i['LastTradePrice'])
    time = i['LastTradeTime']
    timeLong = i['LastTradeDateTimeLong']
    dateTime = i['LastTradeDateTime']
    lastCurrency = i['LastTradeWithCurrency']
    ident = i['ID']


from yahoo_finance import Share
aapl = Share('AAPL')
xlv = Share('XLV')

#aapl = 96.25 02/22/16 290
#xlv = 71.41 04/27/16 1400

prevClose = float(xlv.get_prev_close())

change = (price - prevClose) / prevClose * 100
dayGain = change/100 * (1400 * prevClose)


print symbol + '\t' + time + '\t' + str(price) + '\t' + str(change) + '\t$' + str(dayGain)
