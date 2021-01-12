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
            self._cache = dict()
            self._loadCache()

    def getCurrentPrice(self, ticker: Ticker):
        cache = self._cache[_Field.CURRENT_PRICE]

        if not(ticker.symbol in cache):
            cache[ticker.symbol] =  stockinfo.getLiveData(ticker)
        return cache[ticker.symbol]

    def getLastMonthClosingPrice(self, ticker: Ticker):
        cache = self._cache[_Field.LASTMONTH_PRICE]

        if not(ticker.symbol in cache):
            cache[ticker.symbol] =  stockinfo.getLastMonthClosingPrice(ticker)
        return cache[ticker.symbol]

    def getLastWeekClosingPrice(self, ticker: Ticker):
        cache = self._cache[_Field.LASTWEEK_PRICE]

        if not(ticker.symbol in cache):
            cache[ticker.symbol] =  stockinfo.getLastWeekClosingPrice(ticker)
        return cache[ticker.symbol]

    def getYesterdayClosingPrice(self, ticker: Ticker):
        cache = self._cache[_Field.YESTERDAY_PRICE]

        if not(ticker.symbol in cache):
            cache[ticker.symbol] =  stockinfo.getYesterdayClosingPrice(ticker)
        return cache[ticker.symbol]
    
    @staticmethod
    def clearCache():
        TickerCache.getInstance()._clearCache()

    def _clearCache(self):
        self._cache = dict()
        self._initCache()

    @staticmethod
    def saveCache():
        instance = TickerCache.getInstance()
        instance._saveCache()
    
    def _saveCache(self):
        tickerCacheFile = open(TICKER_CACHE_FILEPATH, "w")
        tickerCacheFile.write(json.dumps(self._cache, indent=2))
        tickerCacheFile.close

    def _loadCache(self):
        self._clearCache()
        if ( not( os.path.isdir(TEMP_DIRECTORY_PATH) and os.path.isfile(TICKER_CACHE_FILEPATH))):
            return False
        
        tickerCacheFile = open(TICKER_CACHE_FILEPATH)
        self._cache = json.loads(tickerCacheFile.read())
        return True
    
    def _initCache(self):
        self._cache[_Field.CURRENT_PRICE] = dict()
        self._cache[_Field.LASTMONTH_PRICE] = dict()
        self._cache[_Field.LASTWEEK_PRICE] = dict()
        self._cache[_Field.YESTERDAY_PRICE] = dict()
        

class _Field:
    CURRENT_PRICE = "CurrentPrice"
    LASTMONTH_PRICE = "LastMonthPrice"
    LASTWEEK_PRICE = "LastWeekPrice"
    YESTERDAY_PRICE = "YesterdayPrice"