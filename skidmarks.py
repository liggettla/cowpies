#!/usr/bin/python
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


