import json, os, sys

from portfolio.portfolio import Portfolio

import stockinfo.stockinfo as si
from stockinfo.ticker import Ticker
from stockinfo.tickerCache import TickerCache

from datetime import datetime
import utils.utils as utils

MINUTES_TO_SECONDS = 60

def main(portfolioJsonFilePath, updateCacheAfterMinutes):
    currentTime = datetime.now()
    currentEpoch = int(currentTime.timestamp())
    lastEpoch = utils.getLastUpdateEpochTime()
    
    print( "Current Time:\t", currentTime.strftime("%Y-%m-%d %H:%M") )

    print("***********************************")
    if isCacheStale(currentEpoch, lastEpoch, updateCacheAfterMinutes * MINUTES_TO_SECONDS):
        print("===Updating Data===")
        utils.setLastUpdateEpochTime(currentEpoch)
        TickerCache.clearCache()
    else:
        print("===Using Cached Data===")


    portfoliosJson = json.loads(utils.getFileData(portfolioJsonFilePath))

    portfolios = list()
    for portfolioJson in portfoliosJson["portfolios"]:
        portfolio = Portfolio()
        portfolio.parse(portfolioJson)
        portfolios.append(portfolio)

    portfolioPrependStr = ""
    Portfolio.printHeader(portfolioPrependStr)
    for portfolio in portfolios:
        portfolio.print(portfolioPrependStr)

    TickerCache.saveCache()

def isCacheStale(currentEpoch, lastEpoch, cacheFreshSeconds):
    print( "Current Epoch:\t", currentEpoch)
    print( "Last Epoch:\t", lastEpoch)

    if currentEpoch < lastEpoch:
        return False
    elif (currentEpoch - lastEpoch) < cacheFreshSeconds:
        return False

    return True

numArgs = len(sys.argv) - 1

# This parses arugments to make sure it's valid
if numArgs == 1:
    main(sys.argv[1], 5)
else:
    print("Improper Usage: Format <portfolio>")
    print("Ex: py3 main.py sample.portfolio")
    exit()