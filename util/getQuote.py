import pandas_datareader.data as web
amzn = web.get_quote_yahoo('AMZN')
print(amzn)
