import sys

import stockinfo.stockinfo as si
from datetime import datetime
import utils.utils as utils

def main(portfolioJson):
    currentTime = datetime.now()
    currentEpoch = int(currentTime.timestamp())
    
    print( "Current Time:\t", currentTime.strftime("%Y-%m-%d %H:%M") )
    print( "Current Epoch:\t", currentEpoch)

    lastEpoch = utils.getLastUpdateEpochTime()

    print( "Last Epoch:\t", lastEpoch)

    print("***********************************")

    UPDATE_DATA = False

    if UPDATE_DATA:
        print("===Updating Data===")
        ticker = 'TSLA'

        print( si.getLiveData(ticker) )

        utils.setLastUpdateEpochTime(currentEpoch)
    else:
        print("===Using Cached Data===")

numArgs = len(sys.argv) - 1

# This parses arugments to make sure it's valid
if numArgs == 1:
    main(sys.argv[1])
else:
    print("Improper Usage: Format <portfolio>")
    print("Ex: py3 main.py sample.portfolio")
    exit()