#!/usr/bin/python
# How to Get a List of all NASDAQ Securities as CSV file using Python?
# +tested in Python 3.5.0b2
#
# (c) 2015 QuantAtRisk.com, by Pawel Lachowicz
#http://www.quantatrisk.com/2015/06/22/get-list-nasdaq-securities-python-csv/

import os

os.system("curl --ftp-ssl anonymous:jupi@jupi.com "
          "ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt "
          "> nasdaq.lst")

os.system("head -20 nasdaq.lst")
print()

os.system("tail -5 nasdaq.lst")
print()

os.system("tail -n +9 nasdaq.lst | cat | sed '$d' | sed 's/|/ /g' > "
          "nasdaq.lst2")

os.system("awk '{print $1}' nasdaq.lst2 > nasdaq.csv")
os.system("echo; head nasdaq.csv; echo '...'; tail nasdaq.csv")

import pandas as pd
data = pd.read_csv("nasdaq.csv", index_col=None, header=None)
data.columns=["Ticker"]
print(data)
