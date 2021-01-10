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

    def getMarketValue(self):
        return self.getPrice() * self.getShares()

    def getPrice(self):
        return TickerCache.getInstance().getCurrentPrice(self.ticker)

    def print(self, prependStr:str):
        defaultColor = TextColor.CWHITE

        marketValueColor = TextColor.CRED
        if self.getMarketValue() > self.getCostBasis():
            marketValueColor = TextColor.CGREEN

        avgPricePaidStr = utils.getStrOutput("avgPricePaid", utils.getDecimalStr(self.getAvgPricePaid()), 8, ' ', defaultColor, defaultColor)
        tickerStr = utils.getStrOutput("Ticker", self.ticker.symbol, 6, ' ', defaultColor, TextColor.CWHITE2)
        costBasisStr = utils.getStrOutput("CostBasis", utils.getDecimalStr(self.getCostBasis()), 12, ' ', defaultColor, defaultColor)
        marketValueStr = utils.getStrOutput("MarketValue", utils.getDecimalStr(self.getMarketValue()), 12, ' ', defaultColor, valueColor=marketValueColor)
        sharesStr = utils.getStrOutput("Shares", utils.getDecimalStr(self.getShares()), 8, ' ', defaultColor, defaultColor)
        priceStr = utils.getStrOutput("Price", utils.getDecimalStr(self.getPrice()), 8, ' ', defaultColor, defaultColor)
        
        output = prependStr + tickerStr + " " + priceStr + " " + marketValueStr + " " + sharesStr + " " + avgPricePaidStr + " " + costBasisStr
        print(output)