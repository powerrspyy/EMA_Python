import yfinance as yf

data = yf.download("AAPL", start='2021-09-01', end='2021-09-11')

print(data)