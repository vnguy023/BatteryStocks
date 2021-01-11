from portfolio.stock import Stock
from portfolio.ledger import Ledger

from stockinfo.ticker import Ticker

import utils.utils as utils
from utils.textColor import TextColor

class Portfolio:
    def __init__(self):
        self._stockDict = dict()
        self.name = ""

    def addLedger(self, ledger: Ledger):
        self._addStock(ledger.ticker)
        stock = self._stockDict.get(ledger.ticker)
        stock.addLedger(ledger)

    def _addStock(self, ticker: Ticker):
        if ticker in self._stockDict:
            return
        
        self._stockDict[ticker] = Stock(ticker)

    def getCostBasis(self):
        costBasis = 0.00
        for value in self._stockDict.values():
            costBasis = costBasis + value.getCostBasis()
        return costBasis

    def getPortfolioValue(self):
        portfolioValue = 0.00
        for value in self._stockDict.values():
            portfolioValue = portfolioValue + value.getMarketValue()
        return portfolioValue


    def parse(self, portfolioDict):
        self.name = portfolioDict['name']

        for ledgerEntry in portfolioDict['ledgers']:
            self.addLedger(Ledger.parse(ledgerEntry))

    def print(self, prependStr):
        stockPrependStr = prependStr + "  "
        ledgerPrependStr = prependStr + "    "
        
        self._print(prependStr)

        Stock.printHeader(stockPrependStr)
        for stock in self._stockDict.values():
            stock.print(stockPrependStr)

            Ledger.printHeader(ledgerPrependStr)
            for ledger in stock.ledgers:
                ledger.print(ledgerPrependStr)

    @classmethod
    def printHeader(cls, prependStr: str):
        defaultColor = TextColor.CYELLOW

        nameStr = utils.getStrValueOutput("{:<24}".format("Portfolio Name"), defaultColor, defaultColor)
        portfolioValueStr = utils.getStrValueOutput("{:^16}".format("Portfolio Value"), defaultColor, defaultColor)
        costBasisStr = utils.getStrValueOutput("{:^16}".format("CostBasis"), defaultColor, defaultColor)

        output = prependStr + nameStr + " " + portfolioValueStr + " " + costBasisStr + " "
        print(output)

    def _print(self, prependStr: str):
        defaultColor = TextColor.CYELLOW

        portfolioValueColor = TextColor.CRED
        if self.getPortfolioValue() > self.getCostBasis():
            portfolioValueColor = TextColor.CGREEN

        nameStr = utils.getStrValueOutput(" " + "{:23}".format(self.name), defaultColor, defaultColor)
        portfolioValueStr = utils.getStrValueOutput("$" + "{:>15}".format(utils.getDecimalStr(self.getPortfolioValue())), defaultColor, portfolioValueColor)
        costBasisStr = utils.getStrValueOutput("$" + "{:>15}".format(utils.getDecimalStr(self.getCostBasis())), defaultColor, defaultColor)

        output = prependStr + nameStr + " " + portfolioValueStr + " " + costBasisStr + " "
        print(output)
