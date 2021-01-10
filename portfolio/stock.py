import utils.utils as utils
from utils.textColor import TextColor

from portfolio.ledger import Ledger

from stockinfo.tickerCache import TickerCache
from stockinfo.ticker import Ticker

class Stock:
    def __init__(self, ticker: Ticker):
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

    def getAvgPricePaid(self):
        return self.getCostBasis() / self.getShares()

    def print(self, prependStr:str):
        ticker = utils.getStrOutput("Ticker", self.ticker.symbol, 6, ' ', defaultColor=TextColor.CWHITE2, valueColor=TextColor.CWHITE2)
        costBasis = utils.getStrOutput("CostBasis", utils.getDecimalStr(self.getCostBasis()), 12, ' ', defaultColor=TextColor.CWHITE2, valueColor=TextColor.CGREEN2)
        shares = utils.getStrOutput("Shares", utils.getDecimalStr(self.getShares()), 8, ' ', defaultColor=TextColor.CWHITE2, valueColor=TextColor.CWHITE2)
        avgPricePaid = utils.getStrOutput("avgPricePaid", utils.getDecimalStr(self.getAvgPricePaid()), 8, ' ', defaultColor=TextColor.CWHITE2, valueColor=TextColor.CWHITE2)
        
        output = prependStr + ticker + " " + shares + " " + avgPricePaid + " " + costBasis
        print(output)