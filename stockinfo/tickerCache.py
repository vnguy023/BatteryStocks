import json, os

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
        if not(ticker.symbol in self._cacheCurrentPrice):
            self._cacheCurrentPrice[ticker.symbol] =  stockinfo.getLiveData(ticker)
        return self._cacheCurrentPrice[ticker.symbol]

    def loadCache(self):
        if ( not( os.path.isdir(TEMP_DIRECTORY_PATH) and os.path.isfile(TICKER_CACHE_FILEPATH))):
            return
        tickerCacheFile = open(TICKER_CACHE_FILEPATH)
        self._cacheCurrentPrice = json.loads(tickerCacheFile.read())
    
    @staticmethod
    def clearCache():
        TickerCache.getInstance()._clearCache()

    def _clearCache(self):
        self._cacheCurrentPrice = dict()

    @staticmethod
    def saveCache():
        instance = TickerCache.getInstance()
        instance._saveCache()
    
    def _saveCache(self):
        tickerCacheFile = open(TICKER_CACHE_FILEPATH, "w")
        tickerCacheFile.write(json.dumps(self._cacheCurrentPrice))
        tickerCacheFile.close