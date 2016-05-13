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
from yahoo_finance import Share

securList =  ['AAPL', 'XLV']
sharesList = {'AAPL':290, 'XLV':1400}
quotes = getQuotes(securList)

#aapl = 96.25 02/22/16 290
#xlv = 71.41 04/27/16 1400
from time import sleep
from os import system
while True:
    system('clear')
    for i in quotes:
        index = i['Index']
        symbol = i['StockSymbol']
        shares = sharesList[symbol]
        price = float(i['LastTradePrice'])
        time = i['LastTradeTime']
        timeLong = i['LastTradeDateTimeLong']
        dateTime = i['LastTradeDateTime']
        lastCurrency = i['LastTradeWithCurrency']
        ident = i['ID']

        stock = Share(str(symbol))
        prevClose = float(stock.get_prev_close())
        dayChange = price - prevClose
        gain = dayChange * shares
        change = (price - prevClose) / prevClose * 100

#Display

        print 'Symbol\tTime\t\tPrice\tClose\t%Change\tTotGain' + \
        '\n' + symbol + '\t' + time + '\t' + str(price) + '\t' + str(prevClose) + \
        '\t' + str(dayChange) + '\t' + str(gain) + '\n'

    sleep(1)


