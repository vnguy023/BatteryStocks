import yfinance as yf
from stockinfo.ticker import Ticker

def getClosingPrice(ticker: Ticker, date):
    tickerData = yf.Ticker(ticker.symbol)
    # pulling historical data
    startDate = "2018-01-07"
    endDate = "2018-01-08"

    data = tickerData.history(start=startDate, end=endDate)
    return data['close']

def getLiveData(ticker: Ticker):
    liveData = yf.download(tickers=ticker.symbol, period='1h', interval='15m', rounding=True)

    #print (liveData)
    return liveData['Close'].values[3]