!pip install yfinance
import yfinance as yf
# 0003.HK
ticker = "YOUR_TICKER"
# Download data for the specified period
data = yf.download(ticker, start="2024-01-01", end="2024-12-31")
# Extract only the date and closing price
date_close_only = data["Close"].reset_index()
date_close_only.columns = ["Date", "Close"]
# Display the data
date_close_only