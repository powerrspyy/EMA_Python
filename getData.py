import yfinance as yf
import pandas as pd

# Define your parameters
symbol = 'AAPL'  # Replace with your desired stock symbol
start_date = '2024-10-21'  # Start date in YYYY-MM-DD format
end_date = '2024-10-25'    # End date in YYYY-MM-DD format
interval = '1m'            # Interval for the data

# Fetch the data
data = yf.download(symbol, start=start_date, end=end_date, interval=interval)

# Extract only the close prices
close_prices_df = data[['Close']]

# Save the DataFrame to a CSV file
close_prices_df.to_csv('close_prices.csv', header=False,  index=False)


