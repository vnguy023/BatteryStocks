import yfinance as yf

def getClosingPrice(ticker, date):
    tickerData = yf.Ticker(ticker)
    # pulling historical data
    startDate = "2018-01-07"
    endDate = "2018-01-08"

    data = tickerData.history(start=startDate, end=endDate)
    return data['close']

def getLiveData(ticker):
    liveData = yf.download(tickers=ticker, period='1h', interval='15m', rounding=True)

    #print (liveData)
    return liveData['Close'].values[3]