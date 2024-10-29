import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file without headers
df = pd.read_csv('close_prices.csv', header=None)

# Convert the first column to a list
close_prices_list = df[0].tolist()

# Function to calculate EMA
def calculate_ema(prices, N):
    multiplier = 2 / (N + 1)
    ema_values = [prices[0]]  # Start with the first price as the initial EMA
    for price in prices[1:]:
        new_ema = (price - ema_values[-1]) * multiplier + ema_values[-1]
        ema_values.append(new_ema)
    return ema_values

# Calculate EMA
ema200 = calculate_ema(close_prices_list, 200)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(close_prices_list, label='Close Price', color='blue', linewidth=1)

# Plot EMA with different colors based on its value
for i in range(1, len(ema200)):
    color = 'green' if ema200[i] < close_prices_list[i] else 'red'
    plt.plot([i-1, i], [ema200[i-1], ema200[i]], color=color, linewidth=1)

# Add titles and labels
plt.title('Exponential Moving Average (EMA)', fontsize=16)
plt.xlabel('Time (minutes)', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add a legend with better visibility
plt.legend(loc='upper left', fontsize=12)

# Add a grid with a lighter style
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Save the plot as an image file
plt.savefig('ema_plot.png', dpi=300, bbox_inches='tight')  # Use bbox_inches='tight' for better layout
plt.close()  # Close the plot if you don't want to display it
