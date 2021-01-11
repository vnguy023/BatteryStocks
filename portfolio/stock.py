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


    def getYesterdayClosingPrice(self):
        return TickerCache.getInstance().getYesterdayClosingPrice(self.ticker)

    def getCostBasis(self):
        result = 0.00
        for ledger in self.ledgers:
            result = result + ledger.getCostBasis()
        return result

    def getShares(self):
        result = 0.00
        for ledger in self.ledgers:
            result = result + ledger.shares
        return result

    def getAvgPricePaid(self):
        return self.getCostBasis() / self.getShares()

    def getMarketValue(self):
        return self.getPrice() * self.getShares()

    def getPrice(self):
        return TickerCache.getInstance().getCurrentPrice(self.ticker)

    @classmethod
    def printHeader(cls, prependStr):
        defaultColor = TextColor.CWHITE
        avgPricePaidStr = utils.getStrValueOutput("{:^14}".format("avgPricePaid"), defaultColor, defaultColor)
        costBasisStr = utils.getStrValueOutput("{:^14}".format("CostBasis"), defaultColor, defaultColor)
        marketValueStr = utils.getStrValueOutput("{:^14}".format("MarketValue"), defaultColor, defaultColor)
        priceStr = utils.getStrValueOutput("{:^14}".format("Current Price"), defaultColor, defaultColor)
        sharesStr = utils.getStrValueOutput("{:^8}".format("Shares"), defaultColor, defaultColor)
        tickerStr = utils.getStrValueOutput("{:^6}".format("Ticker"), defaultColor, defaultColor)
        
        output = prependStr + tickerStr + " " + priceStr + " " + marketValueStr + " " + sharesStr + " " + avgPricePaidStr + " " + costBasisStr
        print(output)

    def print(self, prependStr:str):
        defaultColor = TextColor.CWHITE

        marketValueColor = TextColor.CRED
        if self.getMarketValue() > self.getCostBasis():
            marketValueColor = TextColor.CGREEN

        priceValueColor = TextColor.CRED
        if self.getPrice() > self.getYesterdayClosingPrice():
            priceValueColor = TextColor.CGREEN

        avgPricePaidStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getAvgPricePaid())), defaultColor, defaultColor)
        costBasisStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getCostBasis())), defaultColor, defaultColor)
        marketValueStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getMarketValue())), defaultColor, marketValueColor)
        priceStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getPrice())), defaultColor, priceValueColor)
        sharesStr = utils.getStrValueOutput("{:>8}".format(utils.getDecimalStr(self.getShares())), defaultColor, defaultColor)
        tickerStr = utils.getStrValueOutput("{:>6}".format(self.ticker.symbol), defaultColor, defaultColor)
        
        output = prependStr + tickerStr + " " + priceStr + " " + marketValueStr + " " + sharesStr + " " + avgPricePaidStr + " " + costBasisStr
        print(output)