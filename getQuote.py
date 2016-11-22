# this parses the data returned from yahoo finance for a given stock
# quote and returns a stock object

class getQuote(object):

    def __init__(self, stock, sharesList):
        from yahoo_finance import Share

        self.stock = stock[0]
        self.index = str(self.stock['Index'])
        self.symbol = str(self.stock['StockSymbol'])
        self.shares = int(sharesList[self.symbol])
        self.price = float(self.stock['LastTradePrice'])
        self.time = str(self.stock['LastTradeTime'])
        self.timeLong = str(self.stock['LastTradeDateTimeLong'])
        self.dateTime = str(self.stock['LastTradeDateTime'])
        self.lastCurrency = self.stock['LastTradeWithCurrency']
        self.ident = str(self.stock['ID'])

        # get previous close
        x = Share(self.symbol)
        self.prevClose = float(x.get_prev_close())

        # get changes in stock prices
        self.dayChange = self.price - self.prevClose
        self.gain = self.dayChange * self.shares
        self.change = (self.price - self.prevClose) / self.prevClose * 100

