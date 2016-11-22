# this parses the data returned from yahoo finance for a given stock
# quote and returns a stock object

class getQuote(object):

    def __init__(self, stock, sharesList):
        from yahoo_finance import Share

        self.stock = stock[0]
        self.index = self.stock['Index']
        self.symbol = self.stock['StockSymbol']
        self.shares = sharesList[self.symbol]
        self.price = float(self.stock['LastTradePrice'])
        self.time = self.stock['LastTradeTime']
        self.timeLong = self.stock['LastTradeDateTimeLong']
        self.dateTime = self.stock['LastTradeDateTime']
        self.lastCurrency = self.stock['LastTradeWithCurrency']
        self.ident = self.stock['ID']

        # get previous close
        x = Share(str(self.symbol))
        self.prevClose = float(x.get_prev_close())

        # get changes in stock prices
        self.dayChange = self.price - self.prevClose
        self.gain = self.dayChange * self.shares
        self.change = (self.price - self.prevClose) / self.prevClose * 100

