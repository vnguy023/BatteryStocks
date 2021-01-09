import sys

import stockinfo.stockinfo as si
from datetime import datetime
import utils.utils as utils

MINUTES_TO_SECONDS = 60

def main(portfolioJson, updateCacheAfterMinutes):
    currentTime = datetime.now()
    currentEpoch = int(currentTime.timestamp())
    lastEpoch = utils.getLastUpdateEpochTime()
    
    print( "Current Time:\t", currentTime.strftime("%Y-%m-%d %H:%M") )

    print("***********************************")
    if isCacheStale(currentEpoch, lastEpoch, updateCacheAfterMinutes * MINUTES_TO_SECONDS):
        print("===Updating Data===")
        ticker = 'TSLA'

        print( si.getLiveData(ticker) )

        utils.setLastUpdateEpochTime(currentEpoch)
    else:
        print("===Using Cached Data===")

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