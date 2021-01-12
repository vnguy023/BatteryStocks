import utils.utils as utils
from utils.textColor import TextColor

from stockinfo.ticker import Ticker
from stockinfo.tickerCache import TickerCache

class Ledger:
    def __init__(self, ticker: Ticker, shares: float, pricePaid: float):
        self.ticker = ticker
        self.shares = shares
        self.pricePaid = pricePaid

    @classmethod
    def parse(cls, ledgerDict):
        ticker = Ticker(ledgerDict['ticker'])
        shares = ledgerDict['shares']
        pricePaid = ledgerDict['pricePaid']

        return Ledger(ticker, shares, pricePaid)

    def getCostBasis(self):
        return self.shares * self.pricePaid

    def getMarketValue(self):
        return self.getPrice() * self.shares

    def getPrice(self):
        return TickerCache.getInstance().getCurrentPrice(self.ticker)

    def getYesterdayClosingPrice(self):
        return TickerCache.getInstance().getYesterdayClosingPrice(self.ticker)

    @classmethod
    def printHeader(cls, prependStr:str):
        defaultColor = TextColor.CGREY + TextColor.CBOLD + TextColor.CITALIC
        pricePaidStr = utils.getStrValueOutput("{:^14}".format("PricePaid"), defaultColor, defaultColor)
        costBasisStr = utils.getStrValueOutput("{:^14}".format("CostBasis"), defaultColor, defaultColor)
        marketValueStr = utils.getStrValueOutput("{:^14}".format("MarketValue"), defaultColor, defaultColor)
        sharesStr = utils.getStrValueOutput("{:^10}".format("Shares"), defaultColor, defaultColor)
        priceStr = utils.getStrValueOutput("{:^14}".format("Current Price"), defaultColor, defaultColor)
        
        output = prependStr + priceStr + " " + marketValueStr + " " + sharesStr + " " + pricePaidStr + " " + costBasisStr
        print(output)

    def print(self, prependStr:str):
        defaultColor = TextColor.CGREY + TextColor.CITALIC

        marketValueColor = TextColor.CRED + TextColor.CDIM + TextColor.CITALIC
        if self.getMarketValue() > self.getCostBasis():
            marketValueColor = TextColor.CGREEN + TextColor.CDIM + TextColor.CITALIC

        priceValueColor = TextColor.CRED + TextColor.CDIM + TextColor.CITALIC
        if self.getYesterdayClosingPrice() <= self.getPrice():
            priceValueColor = TextColor.CGREEN + TextColor.CDIM + TextColor.CITALIC

        costBasisStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getCostBasis())), defaultColor, defaultColor)
        marketValueStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getMarketValue())), defaultColor, marketValueColor)
        sharesStr = utils.getStrValueOutput("{:>10}".format(utils.getDecimalStr(self.shares)), defaultColor, defaultColor)
        priceStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getPrice())), defaultColor, priceValueColor)
        pricePaidStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.pricePaid)), defaultColor, defaultColor)
        
        output = prependStr + priceStr + " " + marketValueStr + " " + sharesStr + " " + pricePaidStr + " " + costBasisStr
        print(output)