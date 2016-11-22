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

securList =  ['AAPL', 'XLV', 'QQQ']
sharesList = {'AAPL':290, 'XLV':1400, 'QQQ':232}
quotes = getQuotes(securList)

#aapl = 96.25 02/22/16 290
#xlv = 71.41 04/27/16 1400
#qqq = 116.38 08/31/2016 232
from time import sleep
from os import system
from getQuote import getQuote

while True:
    allOutput = []
    header = 'Symbol\tTime\t\tPrice\tClose\t%Change\tTotGain'
    allOutput.append(header)
    totalGain = 0.0

    for i in securList:
        stock = getQuote(getQuotes(i), sharesList)
        totalGain += stock.gain

        output = '%s\t%s\t%s\t%s\t%s\t%s' % (str(stock.symbol), str(stock.time), str(stock.price), str(stock.prevClose), str(stock.dayChange), str(stock.gain))
        allOutput.append(output)

    sleep(1)
    system('clear')
    for i in allOutput:
        print i
    print 'Total Daily Gain: %f' % (totalGain)
