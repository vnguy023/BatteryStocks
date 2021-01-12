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

    def getAvgPricePaid(self):
        return self.getCostBasis() / self.getShares()

    def getCostBasis(self):
        result = 0.00
        for ledger in self.ledgers:
            result = result + ledger.getCostBasis()
        return result

    def getDayChange(self):
        return self.getPrice() - self.getYesterdayClosingPrice()

    def getLastMonthClosingPrice(self):
        return TickerCache.getInstance().getLastMonthClosingPrice(self.ticker)

    def getLastWeekClosingPrice(self):
        return TickerCache.getInstance().getLastWeekClosingPrice(self.ticker)

    def getMarketValue(self):
        return self.getPrice() * self.getShares()

    def getMonthChange(self):
        return self.getPrice() - self.getLastMonthClosingPrice()

    def getMarketValueLastMonth(self):
        return self.shares * self.getLastMonthClosingPrice()

    def getMarketValueLastWeek(self):
        return self.shares * self.getLastWeekClosingPrice()

    def getMarketValueYesterday(self):
        return self.shares * self.getYesterdayClosingPrice()

    def getPrice(self):
        return TickerCache.getInstance().getCurrentPrice(self.ticker)

    def getShares(self):
        result = 0.00
        for ledger in self.ledgers:
            result = result + ledger.shares
        return result

    def getWeekChange(self):
        return self.getPrice() - self.getLastWeekClosingPrice()

    def getYesterdayClosingPrice(self):
        return TickerCache.getInstance().getYesterdayClosingPrice(self.ticker)

    @classmethod
    def printHeader(cls, prependStr):
        defaultColor = TextColor.CWHITE + TextColor.CBOLD
        avgPricePaidStr = utils.getStrValueOutput("{:^14}".format("avgPricePaid"), defaultColor, defaultColor)
        costBasisStr = utils.getStrValueOutput("{:^14}".format("CostBasis"), defaultColor, defaultColor)
        dayChangeStr = utils.getStrValueOutput("{:^10}".format("DayChange"), defaultColor, defaultColor)
        weekChangeStr = utils.getStrValueOutput("{:^10}".format("WeekChange"), defaultColor, defaultColor)
        monthChangeStr = utils.getStrValueOutput("{:^10}".format("MonthChange"), defaultColor, defaultColor)
        marketValueStr = utils.getStrValueOutput("{:^14}".format("MarketValue"), defaultColor, defaultColor)
        priceStr = utils.getStrValueOutput("{:^14}".format("CurrentPrice"), defaultColor, defaultColor)
        sharesStr = utils.getStrValueOutput("{:^10}".format("Shares"), defaultColor, defaultColor)
        tickerStr = utils.getStrValueOutput("{:^6}".format("Ticker"), defaultColor, defaultColor)
        
        output = prependStr + tickerStr + " " + priceStr + " " + dayChangeStr + " " + marketValueStr + " " + sharesStr + " " + avgPricePaidStr + " " + costBasisStr
        print(output)

    def print(self, prependStr:str):
        defaultColor = TextColor.CWHITE

        marketValueColor = TextColor.CRED
        if self.getMarketValue() > self.getCostBasis():
            marketValueColor = TextColor.CGREEN

        dayChangeColor = TextColor.CRED
        if self.getYesterdayClosingPrice() <= self.getPrice():
            dayChangeColor = TextColor.CGREEN

        weekChangeColor = TextColor.CRED
        if self.getYesterdayClosingPrice() <= self.getPrice():
            weekChangeColor = TextColor.CGREEN
            
        monthChangeColor = TextColor.CRED
        if self.getYesterdayClosingPrice() <= self.getPrice():
            monthChangeColor = TextColor.CGREEN

        avgPricePaidStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getAvgPricePaid())), defaultColor, defaultColor)
        costBasisStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getCostBasis())), defaultColor, defaultColor)
        dayChangeStr = utils.getStrValueOutput("$" + "{:>9}".format(utils.getDecimalStr(self.getDayChange())), defaultColor, dayChangeColor)
        weekChangeStr = utils.getStrValueOutput("$" + "{:>9}".format(utils.getDecimalStr(self.getWeekChange())), defaultColor, weekChangeColor)
        monthChangeStr = utils.getStrValueOutput("$" + "{:>9}".format(utils.getDecimalStr(self.getMonthChange())), defaultColor, monthChangeColor)
        marketValueStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getMarketValue())), defaultColor, marketValueColor)
        priceStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getPrice())), defaultColor, defaultColor)
        sharesStr = utils.getStrValueOutput("{:>10}".format(utils.getDecimalStr(self.getShares())), defaultColor, defaultColor)
        tickerStr = utils.getStrValueOutput("{:6}".format(self.ticker.symbol), defaultColor, defaultColor)
        
        output = prependStr + tickerStr + " " + priceStr + " " + dayChangeStr + " " + marketValueStr + " " + sharesStr + " " + avgPricePaidStr + " " + costBasisStr
        print(output)