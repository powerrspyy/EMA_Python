import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data: Replace this with your own data source
data = {
    'Close': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}
df = pd.DataFrame(data)

# Parameters
N = 5  # Number of periods for the EMA
multiplier = 2 / (N + 1)

# Function to calculate EMA
def calculate_ema(prices, N):
    ema_values = [prices[0]]  # Start with the first price as the initial EMA
    for price in prices[1:]:
        new_ema = (price - ema_values[-1]) * multiplier + ema_values[-1]
        ema_values.append(new_ema)
    return ema_values

# Calculate EMA
df['EMA'] = calculate_ema(df['Close'], N)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(df['Close'], label='Close Price', marker='o')
plt.plot(df['EMA'], label='EMA', linestyle='--', marker='o')
plt.title('Exponential Moving Average (EMA)')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.grid()

# Save the plot as an image file
plt.savefig('ema_plot.png', dpi=300)  # You can change 'ema_plot.png' to your desired filename
plt.close()  # Close the plot if you don't want to display it
