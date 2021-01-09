class Ledger:
    def __init__(self, ticker: str, shares: float, pricePerShare: float):
        self.ticker = ticker
        self.shares = shares
        self.pricePerShare = pricePerShare

    @classmethod
    def parse(cls, ledgerDict):
        ticker = ledgerDict['ticker']
        shares = ledgerDict['shares']
        pricePerShare = ledgerDict['pricePerShare']

        return Ledger(ticker, shares, pricePerShare)

    def print(self, prependStr:str):
        output = prependStr + "[Share="+ str(self.shares).rjust(8, ' ') + "] [PricePerShare=" + str(self.pricePerShare).rjust(8, ' ') + "]"
        print(output)