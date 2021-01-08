import stockinfo.stockinfo as si
from datetime import datetime

currentTime = datetime.now()
epochTotalSeconds = int(currentTime.timestamp())

print( "Current Time", currentTime.strftime("%Y-%m-%d %H:%M") )
print( "Epoch: ", epochTotalSeconds)

ticker = 'TSLA'

print( si.getLiveData(ticker) )