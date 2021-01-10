from stockinfo.ticker import Ticker
from stockinfo import stockinfo

class TickerCache:
    _instance = None

    @staticmethod
    def getInstance():
        if TickerCache._instance == None:
            TickerCache()
        return TickerCache._instance

    def __init__(self):
        if TickerCache._instance is None:
            TickerCache._instance = self
            self._cacheCurrentPrice = dict()

    def getCurrentPrice(self, ticker: Ticker):
        if not(ticker in self._cacheCurrentPrice):
            self._cacheCurrentPrice[ticker] =  stockinfo.getLiveData(ticker)
        return self._cacheCurrentPrice[ticker]