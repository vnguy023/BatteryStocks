from portfolio.ledger import Ledger

class Stock:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.ledgers = list()

    def addLedger(self, ledger: Ledger):
        self.ledgers.append(ledger)