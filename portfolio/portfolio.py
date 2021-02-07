from portfolio.stock import Stock
from portfolio.ledger import Ledger

from stockinfo.ticker import Ticker

import utils.utils as utils
from utils.textColor import TextColor

class Portfolio:
    def __init__(self):
        self._stockDict = dict()
        self.name = ""
        self.hideLedgers = True

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
        result = 0.00
        for value in self._stockDict.values():
            result = result + value.getMarketValue()
        return result

    def getMarketValueYesterday(self):
        result = 0.00
        for value in self._stockDict.values():
            result = result + value.getMarketValueYesterday()
        return result

    def getMarketValueLastWeek(self):
        result = 0.00
        for value in self._stockDict.values():
            result = result + value.getMarketValueLastWeek()
        return result

    def getMarketValueLastMonth(self):
        result = 0.00
        for value in self._stockDict.values():
            result = result + value.getMarketValueLastMonth()
        return result

    def getTotalGain(self):
        return self.getPortfolioValue() - self.getCostBasis()

    def getDayGain(self):
        return self.getPortfolioValue() - self.getMarketValueYesterday()

    def getWeekGain(self):
        return self.getPortfolioValue() - self.getMarketValueLastWeek()

    def getMonthGain(self):
        return self.getPortfolioValue() - self.getMarketValueLastMonth()


    def parse(self, portfolioDict):
        self.name = portfolioDict['name']
        self.hideLedgers = portfolioDict['hideLedgers']

        for ledgerEntry in portfolioDict['ledgers']:
            self.addLedger(Ledger.parse(ledgerEntry))

    def print(self, prependStr):
        stockPrependStr = prependStr + "  "
        ledgerPrependStr = prependStr + "    "
        
        self._print(prependStr)


        stockSeperator = 0
        stockSeperatorStr = stockPrependStr
        for i in range(200):
            stockSeperatorStr = stockSeperatorStr + "="
        Stock.printHeader(stockPrependStr)
        for stock in self._stockDict.values():
            stock.print(stockPrependStr)
            
            stockSeperator = stockSeperator + 1
            if stockSeperator > 5:
                stockSeperator = 0
                print(stockSeperatorStr)
                
            if not self.hideLedgers:
                Ledger.printHeader(ledgerPrependStr)
                for ledger in stock.ledgers:
                    ledger.print(ledgerPrependStr)
            
    @classmethod
    def printHeader(cls, prependStr: str):
        defaultColor = TextColor.CYELLOW + TextColor.CBOLD

        nameStr = utils.getStrValueOutput("{:^24}".format("Portfolio Name"), defaultColor, defaultColor)
        portfolioValueStr = utils.getStrValueOutput("{:^16}".format("Portfolio Value"), defaultColor, defaultColor)
        costBasisStr = utils.getStrValueOutput("{:^16}".format("CostBasis"), defaultColor, defaultColor)

        dayGainStr = utils.getStrValueOutput("{:^14}".format("DayGain"), defaultColor, defaultColor)
        weekGainStr = utils.getStrValueOutput("{:^14}".format("WeekGain"), defaultColor, defaultColor)
        monthGainStr = utils.getStrValueOutput("{:^14}".format("MonthGain"), defaultColor, defaultColor)
        totalGainStr = utils.getStrValueOutput("{:^26}".format("TotalGain"), defaultColor, defaultColor)

        output = prependStr + nameStr + " " + dayGainStr + " " + weekGainStr + " " + monthGainStr + " " + costBasisStr + " " + totalGainStr + " " + portfolioValueStr + " "
        print(output)

    def _print(self, prependStr: str):
        defaultColor = TextColor.CYELLOW

        portfolioValueColor = TextColor.CRED
        if self.getPortfolioValue() > self.getCostBasis():
            portfolioValueColor = TextColor.CGREEN

        totalGainColor = TextColor.CRED
        if self.getTotalGain() > 0:
            totalGainColor = TextColor.CGREEN

        dayGainColor = TextColor.CRED
        if self.getDayGain() > 0:
            dayGainColor = TextColor.CGREEN

        weekGainColor = TextColor.CRED
        if self.getWeekGain() > 0:
            weekGainColor = TextColor.CGREEN

        monthGainColor = TextColor.CRED
        if self.getMonthGain() > 0:
            monthGainColor = TextColor.CGREEN

        nameStr = utils.getStrValueOutput(" " + "{:23}".format(self.name), defaultColor, defaultColor)
        portfolioValueStr = utils.getStrValueOutput("$" + "{:>15}".format(utils.getDecimalStr(self.getPortfolioValue())), defaultColor, portfolioValueColor)
        costBasisStr = utils.getStrValueOutput("$" + "{:>15}".format(utils.getDecimalStr(self.getCostBasis())), defaultColor, defaultColor)

        totalGainStr1 = "$" + "{:>13}".format(utils.getDecimalStr(self.getTotalGain()))
        totalGainStr2 = "{:>12}".format("  " + utils.getDecimalStr(self.getTotalGain()/ self.getCostBasis() * 100) + "%")
        totalGainStr = utils.getStrValueOutput(totalGainStr1 + totalGainStr2, defaultColor, totalGainColor)

        dayGainStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getDayGain())), defaultColor, dayGainColor)
        weekGainStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getWeekGain())), defaultColor, weekGainColor)
        monthGainStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getMonthGain())), defaultColor, monthGainColor)

        output = prependStr + nameStr + " " + dayGainStr + " " + weekGainStr + " " + monthGainStr + " " + costBasisStr + " " + totalGainStr + " " + portfolioValueStr + " "
        print(output)
