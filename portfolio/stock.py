import utils.utils as utils
from utils.textColor import TextColor

from portfolio.ledger import Ledger

class Stock:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.ledgers = list()

    def addLedger(self, ledger: Ledger):
        self.ledgers.append(ledger)

    def getCostBasis(self):
        costBasis = 0.00
        for ledger in self.ledgers:
            costBasis = costBasis + ledger.getCostBasis()
        return costBasis

    def getShares(self):
        shares = 0.00
        for ledger in self.ledgers:
            shares = shares + ledger.shares
        return shares

    def getAvgPricePerShare(self):
        return self.getCostBasis() / self.getShares()

    def print(self, prependStr:str):
        ticker = utils.getStrOutput("Ticker", self.ticker, 6, ' ', defaultColor=TextColor.CWHITE2, valueColor=TextColor.CWHITE2)
        costBasis = utils.getStrOutput("CostBasis", utils.getDecimalStr(self.getCostBasis()), 12, ' ', defaultColor=TextColor.CWHITE2, valueColor=TextColor.CGREEN2)
        shares = utils.getStrOutput("Shares", utils.getDecimalStr(self.getShares()), 8, ' ', defaultColor=TextColor.CWHITE2, valueColor=TextColor.CWHITE2)
        pricePerShare = utils.getStrOutput("AvgPricePerShare", utils.getDecimalStr(self.getAvgPricePerShare()), 8, ' ', defaultColor=TextColor.CWHITE2, valueColor=TextColor.CWHITE2)
        
        output = prependStr + ticker + " " + shares + " " + pricePerShare + " " + costBasis
        print(output)