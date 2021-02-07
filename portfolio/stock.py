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
        return self.getShares() * self.getLastMonthClosingPrice()

    def getMarketValueLastWeek(self):
        return self.getShares() * self.getLastWeekClosingPrice()

    def getMarketValueYesterday(self):
        return self.getShares() * self.getYesterdayClosingPrice()

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

    def getTotalGain(self):
        return self.getMarketValue() - self.getCostBasis()

    def getDayGain(self):
        return self.getMarketValue() - self.getMarketValueYesterday()

    def getWeekGain(self):
        return self.getMarketValue() - self.getMarketValueLastWeek()

    def getMonthGain(self):
        return self.getMarketValue() - self.getMarketValueLastMonth()

    @classmethod
    def printHeader(cls, prependStr):
        defaultColor = TextColor.CWHITE + TextColor.CBOLD
        avgPricePaidStr = utils.getStrValueOutput("{:^14}".format("avgPricePaid"), defaultColor, defaultColor)
        costBasisStr = utils.getStrValueOutput("{:^14}".format("CostBasis"), defaultColor, defaultColor)
        marketValueStr = utils.getStrValueOutput("{:^14}".format("MarketValue"), defaultColor, defaultColor)
        priceStr = utils.getStrValueOutput("{:^10}".format("Price"), defaultColor, defaultColor)
        sharesStr = utils.getStrValueOutput("{:^10}".format("Shares"), defaultColor, defaultColor)
        tickerStr = utils.getStrValueOutput("{:^8}".format("Ticker"), defaultColor, defaultColor)

        dayChangeStr = utils.getStrValueOutput("{:^21}".format("DayChange"), defaultColor, defaultColor)
        weekChangeStr = utils.getStrValueOutput("{:^21}".format("WeekChange"), defaultColor, defaultColor)
        monthChangeStr = utils.getStrValueOutput("{:^21}".format("MonthChange"), defaultColor, defaultColor)

        totalGainStr = utils.getStrValueOutput("{:^26}".format("TotalGain"), defaultColor, defaultColor)
        dayGainStr = utils.getStrValueOutput("{:^14}".format("DayGain"), defaultColor, defaultColor)
        weekGainStr = utils.getStrValueOutput("{:^14}".format("WeekGain"), defaultColor, defaultColor)
        monthGainStr = utils.getStrValueOutput("{:^14}".format("MonthGain"), defaultColor, defaultColor)
        
        output = prependStr + tickerStr + " " + priceStr + " "
        output = output + dayChangeStr + " " + dayGainStr + " " 
        output = output + weekChangeStr + " " + weekGainStr + " " 
        output = output + monthChangeStr + " " + monthGainStr + " " 
        output = output + sharesStr + " " + avgPricePaidStr + " " + costBasisStr
        output = output + marketValueStr + " " + totalGainStr + " " 

        print(output)

    def print(self, prependStr:str):
        defaultColor = TextColor.CWHITE

        marketValueColor = TextColor.CRED
        if self.getMarketValue() > self.getCostBasis():
            marketValueColor = TextColor.CGREEN

        dayChangeColor = TextColor.CRED
        if self.getDayChange() > 0:
            dayChangeColor = TextColor.CGREEN

        weekChangeColor = TextColor.CRED
        if self.getWeekChange() > 0:
            weekChangeColor = TextColor.CGREEN

        monthChangeColor = TextColor.CRED
        if self.getMonthChange() > 0:
            monthChangeColor = TextColor.CGREEN

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

        avgPricePaidStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getAvgPricePaid())), defaultColor, defaultColor)
        if self.getAvgPricePaid() < 1.0:
            avgPricePaidStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getAvgPricePaid(), 4)), defaultColor, defaultColor)
        costBasisStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getCostBasis())), defaultColor, defaultColor)
        marketValueStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getMarketValue())), defaultColor, marketValueColor)
        
        priceStr = utils.getStrValueOutput("$" + "{:>9}".format(utils.getDecimalStr(self.getPrice())), defaultColor, defaultColor)
        if self.getPrice() < 1.0:
            priceStr = utils.getStrValueOutput("$" + "{:>9}".format(utils.getDecimalStr(self.getPrice(), 4)), defaultColor, defaultColor)
        sharesStr = utils.getStrValueOutput("{:>10}".format(utils.getDecimalStr(self.getShares())), defaultColor, defaultColor)
        if self.getShares() < 10.0:
            sharesStr = utils.getStrValueOutput("{:>10}".format(utils.getDecimalStr(self.getShares(), 4)), defaultColor, defaultColor)
        tickerStr = utils.getStrValueOutput("{:8}".format(self.ticker.symbol), defaultColor, defaultColor)

        dayChangeStr1 = "$" + "{:>11}".format(utils.getDecimalStr(self.getDayChange()))
        if abs(self.getDayChange()) < 1.0:
            dayChangeStr1 = "$" + "{:>11}".format(utils.getDecimalStr(self.getDayChange(), 4))
        dayChangeStr2 = "{:>9}".format("  " + utils.getDecimalStr(self.getDayChange()/ self.getYesterdayClosingPrice() * 100) + "%")
        dayChangeStr = utils.getStrValueOutput(dayChangeStr1 + dayChangeStr2, defaultColor, dayChangeColor)

        weekChangeStr1 = "$" + "{:>11}".format(utils.getDecimalStr(self.getWeekChange()))
        if abs(self.getWeekChange()) < 1.0:
            weekChangeStr1 = "$" + "{:>11}".format(utils.getDecimalStr(self.getWeekChange(), 4))
        weekChangeStr2 = "{:>9}".format("  " + utils.getDecimalStr(self.getWeekChange()/ self.getLastWeekClosingPrice() * 100) + "%")
        weekChangeStr = utils.getStrValueOutput(weekChangeStr1 + weekChangeStr2, defaultColor, weekChangeColor)

        monthChangeStr1 = "$" + "{:>11}".format(utils.getDecimalStr(self.getMonthChange()))
        if abs(self.getMonthChange()) < 1.0:
            monthChangeStr1 = "$" + "{:>11}".format(utils.getDecimalStr(self.getMonthChange(), 4))
        monthChangeStr2 = "{:>9}".format("  " + utils.getDecimalStr(self.getMonthChange()/ self.getLastMonthClosingPrice() * 100) + "%")
        monthChangeStr = utils.getStrValueOutput(monthChangeStr1 + monthChangeStr2, defaultColor, monthChangeColor)

        totalGainStr1 = "$" + "{:>13}".format(utils.getDecimalStr(self.getTotalGain()))
        totalGainStr2 = "{:>12}".format("  " + utils.getDecimalStr(self.getTotalGain()/ self.getCostBasis() * 100) + "%")
        totalGainStr = utils.getStrValueOutput(totalGainStr1 + totalGainStr2, defaultColor, totalGainColor)

        dayGainStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getDayGain())), defaultColor, dayGainColor)
        weekGainStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getWeekGain())), defaultColor, weekGainColor)
        monthGainStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getMonthGain())), defaultColor, monthGainColor)
        
        output = prependStr + tickerStr + " " + priceStr + " "
        output = output + dayChangeStr + " " + dayGainStr + " " 
        output = output + weekChangeStr + " " + weekGainStr + " " 
        output = output + monthChangeStr + " " + monthGainStr + " " 
        output = output + sharesStr + " " + avgPricePaidStr + " " + costBasisStr
        output = output + marketValueStr + " " + totalGainStr + " " 
        print(output)