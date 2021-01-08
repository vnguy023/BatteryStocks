import yfinance as yf

tslaData = yf.Ticker('TSLA')

print(tslaData.info)