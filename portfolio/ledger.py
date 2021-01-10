import utils.utils as utils
from utils.textColor import TextColor

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

    def getCostBasis(self):
        return self.shares * self.pricePerShare

    def print(self, prependStr:str):
        costBasis = utils.getStrOutput("CostBasis", utils.getDecimalStr(self.getCostBasis()), 12, ' ', TextColor.CGREEN)
        shares = utils.getStrOutput("Shares", utils.getDecimalStr(self.shares), 8, ' ')
        pricePerShare = utils.getStrOutput("PricePerShare", utils.getDecimalStr(self.pricePerShare), 8, ' ')
        
        output = prependStr + shares + " " + pricePerShare + " " + costBasis
        print(output)