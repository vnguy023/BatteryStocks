from datetime import datetime, timedelta
import pytz

import yfinance as yf
from stockinfo.ticker import Ticker

class StockInfo: 
    _instance = None

    @staticmethod
    def getInstance():
        if StockInfo._instance == None:
            StockInfo()
        return StockInfo._instance

    def __init__(self):
        if StockInfo._instance is None:
            StockInfo._instance = self
            self._tickerData = dict()

    def getTickerData(self, ticker: Ticker):
        if not (ticker in self._tickerData):
            self._tickerData[ticker] = yf.Ticker(ticker.symbol)
        return self._tickerData[ticker]

def getYesterdayClosingPrice(ticker: Ticker):
    #print("[Desc=Hitting Server] [getYesterdayClosingPrice] [Ticker={ticker}]".format(ticker=ticker.symbol))

    tickerData = StockInfo.getInstance().getTickerData(ticker)
    return float(tickerData.info['previousClose'])

def getLastMonthClosingPrice(ticker: Ticker):
    #print("[Desc=Hitting Server] [getLastWeekClosingPrice] [Ticker={ticker}]".format(ticker=ticker.symbol))

    periodDays = 30
    currentTime = datetime.now()
    startDate = (currentTime - timedelta(days=periodDays)).strftime("%Y-%m-%d")
    endDate = (currentTime - timedelta(days=periodDays - 25)).strftime("%Y-%m-%d")

    tickerData = StockInfo.getInstance().getTickerData(ticker)
    data = tickerData.history(start=startDate, end=endDate)

    index = 0
    if len(data) <= 0:
        print("[Error=No Data] [Ticker={Ticker}]".format(Ticker=ticker.symbol))
        return 0.00

    return data['Close'].values[index]

def getLastWeekClosingPrice(ticker: Ticker):
    #print("[Desc=Hitting Server] [getLastWeekClosingPrice] [Ticker={ticker}]".format(ticker=ticker.symbol))

    periodDays = 7
    currentTime = datetime.now()
    startDate = (currentTime - timedelta(days=periodDays)).strftime("%Y-%m-%d")
    endDate = currentTime.strftime("%Y-%m-%d")

    tickerData = StockInfo.getInstance().getTickerData(ticker)
    data = tickerData.history(start=startDate, end=endDate)

    index = 0
    if len(data) <= 0:
        print("[Error=No Data] [Ticker={Ticker}]".format(Ticker=ticker.symbol))
        return 0.00

    return data['Close'].values[index]

def getLiveData(ticker: Ticker):
    #print("[Desc=Hitting Server] [getLiveData] [Ticker={ticker}]".format(ticker=ticker.symbol))

    data = yf.download(tickers=ticker.symbol, period='1d', interval='1d', rounding=False, progress=False)

    lastIndex = len(data) - 1
    if lastIndex < 0:
        print("[Error=No Data] [Ticker={Ticker}]".format(Ticker=ticker.symbol))
        return 0.00

    return data['Close'].values[lastIndex]