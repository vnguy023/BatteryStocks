import os

from stockinfo.ticker import Ticker
from stockinfo import stockinfo

from utils.utils import TEMP_DIRECTORY_PATH

TICKER_CACHE_FILENAME = "TickerCache.txt"
TICKER_CACHE_FILEPATH = os.path.join(TEMP_DIRECTORY_PATH, TICKER_CACHE_FILENAME)

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

            self.loadCache()

    def getCurrentPrice(self, ticker: Ticker):
        if not(ticker in self._cacheCurrentPrice):
            self._cacheCurrentPrice[ticker] =  stockinfo.getLiveData(ticker)
        return self._cacheCurrentPrice[ticker]

    def loadCache(self):
        if ( not( os.path.isdir(TEMP_DIRECTORY_PATH) and os.path.isfile(TICKER_CACHE_FILENAME))):
            return

    @staticmethod
    def saveCache():
        instance = TickerCache.getInstance()
        instance._saveCache()
    
    def _saveCache(self):
        value = "Hello World"

        tickerCacheFile = open(TICKER_CACHE_FILEPATH, "w")
        tickerCacheFile.write(str(value))
        tickerCacheFile.close