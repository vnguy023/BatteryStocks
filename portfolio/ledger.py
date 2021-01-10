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

    def print(self, prependStr:str):
        defaultColor = TextColor.CGREY

        marketValueColor = TextColor.CRED
        if self.getMarketValue() > self.getCostBasis():
            marketValueColor = TextColor.CGREEN

        costBasisStr = utils.getStrOutput("CostBasis", utils.getDecimalStr(self.getCostBasis()), 12, ' ', defaultColor, defaultColor)
        marketValueStr = utils.getStrOutput("MarketValue", utils.getDecimalStr(self.getMarketValue()), 12, ' ', defaultColor=TextColor.CGREY, valueColor=marketValueColor)
        sharesStr = utils.getStrOutput("Shares", utils.getDecimalStr(self.shares), 8, ' ', defaultColor, defaultColor)
        priceStr = utils.getStrOutput("Price", utils.getDecimalStr(self.getPrice()), 8, ' ', defaultColor, defaultColor)
        pricePaidStr = utils.getStrOutput("PricePaid", utils.getDecimalStr(self.pricePaid), 8, ' ', defaultColor, defaultColor)
        
        output = prependStr + priceStr + " " + marketValueStr + " " + sharesStr + " " + pricePaidStr + " " + costBasisStr
        print(output)