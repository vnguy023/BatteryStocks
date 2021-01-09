from portfolio.stock import Stock
from portfolio.ledger import Ledger

class Portfolio:
    def __init__(self):
        self._stockDict = dict()
        self.name = ""

    def addLedger(self, ledger: Ledger):
        self._addStock(ledger.ticker)
        stock = self._stockDict.get(ledger.ticker)
        stock.addLedger(ledger)

    def _addStock(self, ticker: str):
        if ticker in self._stockDict:
            return
        
        self._stockDict[ticker] = Stock(ticker)

    def parse(self, portfolioDict):
        self.name = portfolioDict['name']

        for ledgerEntry in portfolioDict['ledgers']:
            self.addLedger(Ledger.parse(ledgerEntry))

    def print(self):
        print("////////////////////////////////////")
        print("//// ", self.name)
        print("////////////////////////////////////")

        for stock in self._stockDict.values():
            print("Ticker:", stock.ticker)
            
            for ledger in stock.ledgers:
                ledger.print("\t")