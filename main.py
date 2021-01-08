import stockinfo.stockinfo as si
from datetime import datetime
import utils.utils as utils

currentTime = datetime.now()
currentEpoch = int(currentTime.timestamp())

print( "Current Time", currentTime.strftime("%Y-%m-%d %H:%M") )
print( "CurrentEpoch: ", currentEpoch)


lastEpoch = utils.getLastUpdateEpochTime()

ticker = 'TSLA'

print( si.getLiveData(ticker) )

utils.setLastUpdateEpochTime(currentEpoch)