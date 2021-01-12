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

    def getDayChange(self):
        return self.getPrice() - self.getYesterdayClosingPrice()

    def getLastMonthClosingPrice(self):
        return TickerCache.getInstance().getLastMonthClosingPrice(self.ticker)

    def getLastWeekClosingPrice(self):
        return TickerCache.getInstance().getLastWeekClosingPrice(self.ticker)

    def getMarketValue(self):
        return self.getPrice() * self.shares

    def getMarketValueLastMonth(self):
        return self.shares * self.getLastMonthClosingPrice()

    def getMarketValueLastWeek(self):
        return self.shares * self.getLastWeekClosingPrice()

    def getMarketValueYesterday(self):
        return self.shares * self.getYesterdayClosingPrice()

    def getMonthChange(self):
        return self.getPrice() - self.getLastMonthClosingPrice()

    def getPrice(self):
        return TickerCache.getInstance().getCurrentPrice(self.ticker)
        
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
    def printHeader(cls, prependStr:str):
        defaultColor = TextColor.CGREY + TextColor.CBOLD + TextColor.CITALIC
        
        costBasisStr = utils.getStrValueOutput("{:^14}".format("CostBasis"), defaultColor, defaultColor)
        marketValueStr = utils.getStrValueOutput("{:^14}".format("MarketValue"), defaultColor, defaultColor)
        sharesStr = utils.getStrValueOutput("{:^10}".format("Shares"), defaultColor, defaultColor)
        pricePaidStr = utils.getStrValueOutput("{:^14}".format("PricePaid"), defaultColor, defaultColor)

        totalGainStr = utils.getStrValueOutput("{:^14}".format("TotalGain"), defaultColor, defaultColor)
        dayGainStr = utils.getStrValueOutput("{:^14}".format("DayGain"), defaultColor, defaultColor)
        weekGainStr = utils.getStrValueOutput("{:^14}".format("WeekGain"), defaultColor, defaultColor)
        monthGainStr = utils.getStrValueOutput("{:^14}".format("MonthGain"), defaultColor, defaultColor)
        
        output = prependStr + sharesStr + " " + pricePaidStr + " " + costBasisStr + " " + marketValueStr + " "
        output = output + totalGainStr + " " + dayGainStr + " " + weekGainStr + " " + monthGainStr + " "
        print(output)

    def print(self, prependStr:str):
        defaultColor = TextColor.CGREY + TextColor.CITALIC

        marketValueColor = TextColor.CRED + TextColor.CDIM + TextColor.CITALIC
        if self.getMarketValue() > self.getCostBasis():
            marketValueColor = TextColor.CGREEN + TextColor.CDIM + TextColor.CITALIC

        totalGainColor = TextColor.CRED + TextColor.CDIM + TextColor.CITALIC
        if self.getTotalGain() > 0:
            totalGainColor = TextColor.CGREEN + TextColor.CDIM + TextColor.CITALIC

        dayGainColor = TextColor.CRED + TextColor.CDIM + TextColor.CITALIC
        if self.getDayGain() > 0:
            dayGainColor = TextColor.CGREEN + TextColor.CDIM + TextColor.CITALIC

        weekGainColor = TextColor.CRED + TextColor.CDIM + TextColor.CITALIC
        if self.getWeekGain() > 0:
            weekGainColor = TextColor.CGREEN + TextColor.CDIM + TextColor.CITALIC

        monthGainColor = TextColor.CRED + TextColor.CDIM + TextColor.CITALIC
        if self.getMonthGain() > 0:
            monthGainColor = TextColor.CGREEN + TextColor.CDIM + TextColor.CITALIC

        costBasisStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getCostBasis())), defaultColor, defaultColor)
        marketValueStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getMarketValue())), defaultColor, marketValueColor)
        sharesStr = utils.getStrValueOutput("{:>10}".format(utils.getDecimalStr(self.shares)), defaultColor, defaultColor)
        pricePaidStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.pricePaid)), defaultColor, defaultColor)
        
        totalGainStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getTotalGain())), defaultColor, totalGainColor) 
        dayGainStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getDayGain())), defaultColor, dayGainColor)
        weekGainStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getWeekGain())), defaultColor, weekGainColor)
        monthGainStr = utils.getStrValueOutput("$" + "{:>13}".format(utils.getDecimalStr(self.getMonthGain())), defaultColor, monthGainColor)

        output = prependStr + sharesStr + " " + pricePaidStr + " " + costBasisStr + " " + marketValueStr + " "
        output = output + totalGainStr + " " + dayGainStr + " " + weekGainStr + " " + monthGainStr + " "
        print(output)